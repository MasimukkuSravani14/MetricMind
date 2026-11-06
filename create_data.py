import os
import pandas as pd

# Create data folder automatically
os.makedirs("data", exist_ok=True)

# Sales dataset
data = {
    "date": [
        "2025-01-10",
        "2025-01-15",
        "2025-02-05",
        "2025-02-15",
        "2025-03-10",
        "2025-03-20",
        "2025-04-10",
        "2025-04-18",
        "2025-05-05",
        "2025-05-20",
        "2025-06-10",
        "2025-06-25"
    ],

    "country": [
        "Germany",
        "France",
        "India",
        "Japan",
        "Germany",
        "Italy",
        "France",
        "Spain",
        "India",
        "China",
        "Germany",
        "France"
    ],

    "region": [
        "Europe",
        "Europe",
        "Asia",
        "Asia",
        "Europe",
        "Europe",
        "Europe",
        "Europe",
        "Asia",
        "Asia",
        "Europe",
        "Europe"
    ],

    "product": [
        "Laptop",
        "Phone",
        "Laptop",
        "Phone",
        "Laptop",
        "Tablet",
        "Phone",
        "Laptop",
        "Tablet",
        "Phone",
        "Laptop",
        "Phone"
    ],

    "revenue": [
        50000,
        40000,
        60000,
        55000,
        45000,
        42000,
        48000,
        52000,
        58000,
        62000,
        46000,
        43000
    ],

    "material_cost": [
        28000,
        22000,
        30000,
        29000,
        27000,
        25000,
        29000,
        31000,
        30000,
        34000,
        30000,
        28000
    ],

    "shipping_cost": [
        4000,
        3500,
        3000,
        4500,
        5000,
        4000,
        5500,
        6000,
        3500,
        5000,
        6000,
        5500
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save dataset as CSV
df.to_csv("data/sales.csv", index=False)

# Display success message
print("Sales dataset created successfully!")
print(df)