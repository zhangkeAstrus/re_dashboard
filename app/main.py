from fastapi import FastAPI
from app.api.v1.routes import users, site_visits, observations, observation_templates, hazards

app = FastAPI(title="RE Dashboard API")

app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(site_visits.router, prefix="/api/v1/site_visits", tags=["Site Visits"])
app.include_router(observations.router, prefix="/api/v1/observations", tags=["Observations"])
app.include_router(observation_templates.router, prefix="/api/v1/templates", tags=["Observation Templates"])
app.include_router(hazards.router, prefix="/api/v1/hazards", tags=["Hazards"])

