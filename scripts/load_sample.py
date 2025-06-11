import sys
import os
import pandas as pd

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.db.session import SessionLocal
from app.db.models.hazard import Hazard  # Adjust if model is elsewhere

# Path to your Excel file
excel_path = r"C:\Users\kzhang2\projects\scripts\re_dashboard data\data samples\Hazard Category Data Source.xlsx"

# Load Excel (adjust sheet name and column as needed)
df = pd.read_excel(excel_path, sheet_name=0)  # or specify the sheet name
print(df.columns)  # print to see column names

# Assuming the column with hazard names is called "Hazard Name"
hazard_names = df["Hazard Category"].dropna().unique()

db = SessionLocal()

for name in hazard_names:
    # Optional: skip if already exists
    exists = db.query(Hazard).filter(Hazard.name == name).first()
    if not exists:
        db.add(Hazard(name=name))

db.commit()
db.close()

print("✅ Hazard data loaded successfully.")
