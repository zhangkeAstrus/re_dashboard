import streamlit as st
import requests
from datetime import date

API_BASE = "http://localhost:8000/api/v1"
st.set_page_config(page_title="RE Dashboard", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("🔧 Navigation")
page = st.sidebar.radio("Go to", ["📊 Dashboard", "📝 Log New Site Visit"])

st.title("🏗️ Risk Engineering Dashboard")

# --- Dashboard Page ---
if page == "📊 Dashboard":
    st.header("📅 Past Site Visits")

    visits_resp = requests.get(f"{API_BASE}/site_visits/")
    if visits_resp.status_code == 200:
        visits = visits_resp.json()
        for visit in visits:
            with st.expander(f"🔹 {visit['site_name']} — {visit['visit_date']} (ID: {visit['id']})"):
                st.markdown(f"**Engineer ID:** {visit['engineer_id']}")
                st.markdown(f"**Notes:** {visit.get('notes', 'No notes')}")

                obs_resp = requests.get(f"{API_BASE}/observations/")
                if obs_resp.status_code == 200:
                    obs_list = [obs for obs in obs_resp.json() if obs["site_visit_id"] == visit["id"]]
                    if obs_list:
                        for obs in obs_list:
                            st.markdown(f"- 🔸 **{obs['title']}** ({obs['severity']})")
                            st.caption(obs['description'])
                    else:
                        st.info("No observations recorded for this visit.")
    else:
        st.error("Failed to fetch site visits.")

# --- Log New Visit Page ---
elif page == "📝 Log New Site Visit":
    st.header("📝 Log a New Site Visit")

    if "active_visit_id" not in st.session_state:
        st.session_state.active_visit_id = None

    if not st.session_state.active_visit_id:
        with st.form("visit_form"):
            site_name = st.text_input("Site Name")
            visit_date = st.date_input("Visit Date", value=date.today())
            engineer_id = st.number_input("Engineer ID", min_value=1, step=1)
            notes = st.text_area("Visit Notes (optional)")
            submitted = st.form_submit_button("Submit Site Visit")

        if submitted:
            visit_payload = {
                "site_name": site_name,
                "visit_date": str(visit_date),
                "engineer_id": int(engineer_id),
                "notes": notes
            }
            visit_resp = requests.post(f"{API_BASE}/site_visits/", json=visit_payload)
            if visit_resp.status_code == 200:
                st.session_state.active_visit_id = visit_resp.json()["id"]
                st.success(f"Visit logged! You can now add multiple observations.")
                st.rerun() # 🔁 This forces Streamlit to reload with updated state
            else:
                st.error("Failed to submit site visit.")
    else:
        visit_id = st.session_state.active_visit_id
        st.info(f"Logging observations for Visit ID: {visit_id}")
        st.button("🔁 Start New Visit", on_click=lambda: st.session_state.pop("active_visit_id"))

        st.subheader("➕ Add Observation")

        # Fetch templates
        template_resp = requests.get(f"{API_BASE}/templates/")
        templates = template_resp.json() if template_resp.status_code == 200 else []
        template_titles = [f"{t['id']}: {t['title']}" for t in templates]
        selected_template = st.selectbox("Start from Template (optional)", ["None"] + template_titles)

        prefill = {}
        if selected_template != "None":
            selected_id = int(selected_template.split(":")[0])
            prefill = next((t for t in templates if t["id"] == selected_id), {})
        else:
            selected_id = None

        # Fetch hazard list
        hazard_resp = requests.get(f"{API_BASE}/hazards/")
        hazards = hazard_resp.json() if hazard_resp.status_code == 200 else []
        hazard_names = [h["name"] for h in hazards]
        hazard_selection = st.selectbox("Hazard Category", hazard_names + ["Other"])

        # Optional custom hazard
        custom_hazard = None
        if hazard_selection == "Other":
            custom_hazard = st.text_input("Enter custom hazard")
        final_hazard = custom_hazard if hazard_selection == "Other" else hazard_selection

        action_type_options = ["Corrective", "Positive"]

        with st.form("observation_form"):
            title = st.text_input("Observation Title", value=prefill.get("title", ""))
            description = st.text_area("Description", value=prefill.get("description", ""))
            action_type = st.selectbox("Action Type", action_type_options, index=0)
            recommendation = st.text_area("Recommendation", value=prefill.get("recommendation", ""))
            photo = st.file_uploader("Attach a photo (optional)", type=["png", "jpg", "jpeg"])
            obs_submit = st.form_submit_button("Submit Observation")

        if obs_submit:
            # Construct form data
            form_data = {
                "site_visit_id": str(visit_id),
                "title": title,
                "description": description,
                "action_type": action_type,
                "hazard": final_hazard,
                "recommendation": recommendation,
                "template_id": str(selected_id) if selected_id else "",
                "original_observation_id": "",
            }

            files = {"photo": photo} if photo else None

            obs_resp = requests.post(
                f"{API_BASE}/observations/",
                data=form_data,
                files=files
            )

            if obs_resp.status_code == 200:
                st.success("✅ Observation added with photo!" if photo else "✅ Observation added!")
            else:
                st.error(f"❌ Failed to submit observation. {obs_resp.text}")


