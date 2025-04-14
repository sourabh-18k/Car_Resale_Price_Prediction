import pandas as pd
import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt

data = pd.read_csv("data/car_resale_prices.csv")

df = data.copy()


df = df.drop(columns=["Unnamed: 0"], errors="ignore")

df.drop(columns=["insurance", "city"], inplace=True)


df["max_power"].str.replace("bhp", "", regex=True)
df["mileage"].str.replace(" kmpl", "", regex=True)

# Function to convert resale_price to integer
def convert_resale_price(value):
    if isinstance(value, str):
        value = value.replace("₹", "").replace(",", "").strip()

        if "Crore" in value:
            return int(float(value.replace("Crore", "").strip()) * 10000000)
        elif "Lakh" in value:
            return int(float(value.replace("Lakh", "").strip()) * 100000)
        elif value.isdigit():
            return int(value)
    return None

# Apply conversion to resale_price column
df["resale_price"] = df["resale_price"].apply(convert_resale_price)

import re



# Function to extract only the year from different formats
def extract_year(value):
    if pd.isnull(value):
        return None  # Keep NaN values
    match = re.search(r"\b(20\d{2}|\d{2})\b", str(value))  # Extract 4-digit or 2-digit year
    if match:
        year = match.group(0)
        if len(year) == 2:  # Convert 2-digit year to 4-digit (assuming all are 2000s)
            year = "20" + year
        return int(year)
    return None

# Apply the function to clean the 'registered_year' column
df["registered_year"] = df["registered_year"].apply(extract_year)

df = df[df["registered_year"].notna()]

df["registered_year"] = df["registered_year"].astype("int")

df[df["seats"].isnull()]

df = df[df["registered_year"].notna()]
df = df[df["kms_driven"].notna()]
df = df[df["engine_capacity"].notna()]
df = df[df["max_power"].notna()]
df = df[df["seats"].notna()]

df["mileage"] = df["mileage"].str.extract(r"([\d\.]+)").astype(float)

# Fill missing mileage values using the median mileage of the same car model
df["mileage"] = df["mileage"].fillna(df.groupby("full_name")["mileage"].transform("median"))

# Fill remaining NaN values with the overall median mileage
df["mileage"] = df["mileage"].fillna(df["mileage"].median())

df["kms_driven"] = df["kms_driven"].str.replace(" Kms", "").str.replace(",", "").astype(float)

df["max_power"] = df["max_power"].str.extract(r"(\d+\.?\d*)").astype(float)

df["kms_driven"] = df["kms_driven"].astype("int")

df["engine_capacity"] = df["engine_capacity"].str.replace(" cc", "", regex=True).astype(int)

# Define valid body types
valid_body_types = ["Hatchback", "Sedan", "SUV", "MUV", "Minivan", "Pickup", "Coupe", "Wagon", "Convertibles"]

# Replace incorrect body types with NaN
df["body_type"] = df["body_type"].apply(lambda x: x if x in valid_body_types else None)

df["body_type"] = df.groupby("full_name")["body_type"].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else x))

df["body_type"] = df["body_type"].fillna(df["body_type"].mode()[0])


df = pd.get_dummies(df, columns=["transmission_type", "fuel_type", "body_type"], drop_first=True)



# Split "full_name" into components without limiting splits
split_values = df['full_name'].str.split()

# Extract brand (second component) and model (remaining components after brand)
df['brand'] = split_values.str[1]
df['model'] = split_values.str[2:].str.join(' ')  # Join remaining parts into a single string

# Clean Model name: Remove engine sizes/trim codes (e.g., "1.2 Alpha", "XTA")
df['model'] = df['model'].str.replace(r'\s\d+\.\d+.*|\s[A-Z]{2,}.*', '', regex=True)


brand_avg_price = df.groupby('brand')['resale_price'].mean().to_dict()
df['brand_encoded'] = df['brand'].map(brand_avg_price)

# Frequency encoding for model
model_freq = df['model'].value_counts(normalize=True).to_dict()
df['model_freq'] = df['model'].map(model_freq)


df.drop(columns=["full_name","brand","model"], inplace=True)

owner_mapping = {"First Owner": 1, "Second Owner": 2, "Third Owner": 3, "Fourth Owner": 4, "Fifth Owner": 5}
df["owner_type"] = df["owner_type"].map(owner_mapping)

df['resale_price'] = np.log1p(df['resale_price'])


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
numerical_cols = ["registered_year", "engine_capacity", "kms_driven", "max_power", "seats", "mileage"]
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

df.to_csv("data/cleaned_preprocessed.csv", index=False)



