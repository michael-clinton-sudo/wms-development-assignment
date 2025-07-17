
import pandas as pd

def process_file(file_path):
    df = pd.read_excel(file_path) if file_path.endswith(".xlsx") else pd.read_csv(file_path)
    df.dropna(how="all", inplace=True)
    df.columns = [col.strip() for col in df.columns]
    df["SKU"] = df["SKU"].str.strip()

    skus = pd.read_csv("sample_data/skus.csv")
    combos = pd.read_csv("sample_data/combos.csv")

    df = df.merge(skus, on="SKU", how="left")

    expanded_rows = []
    for _, row in df.iterrows():
        if row["SKU"] in combos["Combo"].values:
            components = combos[combos["Combo"] == row["SKU"]]["Component"].values[0].split("+")
            for comp in components:
                new_row = row.copy()
                new_row["SKU"] = comp.strip()
                expanded_rows.append(new_row)
        else:
            expanded_rows.append(row)

    cleaned_df = pd.DataFrame(expanded_rows)
    return cleaned_df
