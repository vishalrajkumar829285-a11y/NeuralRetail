import pandas as pd

def clean_data(file_path):
    # Load dataset
    df = pd.read_excel(file_path)

    print("=" * 50)
    print("ORIGINAL DATASET")
    print("=" * 50)
    print("Shape:", df.shape)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows where CustomerID is missing
    df = df.dropna(subset=["CustomerID"])

    # Remove negative or zero Quantity
    df = df[df["Quantity"] > 0]

    # Remove negative or zero UnitPrice
    df = df[df["UnitPrice"] > 0]

    print("\nData Cleaning Completed Successfully!")
    print("Cleaned Shape:", df.shape)

    return df