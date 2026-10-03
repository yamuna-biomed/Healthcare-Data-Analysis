import pandas as pd

# Load your data
df = pd.read_csv('C:\\Users\\Divya\\Documents\\GitHub\\Healthcare-Data-Analysis\\data\\Pharma_data.csv', encoding='latin-1')

print("=" * 60)
print("PHARMACEUTICAL DATA OVERVIEW")
print("=" * 60)
print(f"Total products: {len(df)}")
print(f"Total columns: {len(df.columns)}\n")

print("Column names:")
for col in df.columns:
    print(f"  - {col}")
print()

print("=" * 60)
print("CHECKING FOR PROBLEMS")
print("=" * 60)

# Missing values
print("Missing values in each column:")
missing = df.isnull().sum()
print(missing)
print()

# Duplicates
duplicates_before = len(df)
print(f"Total rows before removing duplicates: {duplicates_before}")

df = df.drop_duplicates()

duplicates_after = len(df)
print(f"Total rows after removing duplicates: {duplicates_after}")
print(f"Duplicate rows removed: {duplicates_before - duplicates_after}\n")

print("=" * 60)
print("DATA ANALYSIS")
print("=" * 60)
print(f"Total unique products: {len(df)}\n")

# Top manufacturers
print("Top 10 manufacturers (LABELERNAME):")
manufacturers = df['LABELERNAME'].value_counts().head(10)
for mfg, count in manufacturers.items():
    percentage = (count / len(df)) * 100
    print(f"  {mfg}: {count} products ({percentage:.1f}%)")
print()

# Top dosage forms
print("Top 10 dosage forms (DOSAGEFORMNAME):")
dosages = df['DOSAGEFORMNAME'].value_counts().head(10)
for dosage, count in dosages.items():
    print(f"  {dosage}: {count} products")
print()

# Top routes
print("Top 10 routes of administration (ROUTENAME):")
routes = df['ROUTENAME'].value_counts().head(10)
for route, count in routes.items():
    print(f"  {route}: {count} products")
print()

# Save cleaned data
df.to_csv('C:\\Users\\Divya\\Documents\\GitHub\\Healthcare-Data-Analysis\\data\\Pharma_data_cleaned.csv', index=False)
print("✓ Cleaned data saved to: data/Pharma_data_cleaned.csv")