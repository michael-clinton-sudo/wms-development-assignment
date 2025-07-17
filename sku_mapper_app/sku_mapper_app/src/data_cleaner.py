import pandas as pd
from src.mapper import SKUMapper
from src.combo_handler import ComboHandler

class SalesDataCleaner:
    def __init__(self, sales_file, mapper, combo_handler, log_path):
        self.df = pd.read_csv(sales_file)
        self.mapper = mapper
        self.combo_handler = combo_handler
        self.log_path = log_path
        self.cleaned = []

    def process(self):
        for _, row in self.df.iterrows():
            raw_msku = row['MSKU']
            mapped_msku = self.mapper.map_sku(raw_msku)
            combo_parts = self.combo_handler.get_combo_components(raw_msku)

            if mapped_msku:
                combo_flag = "No"
                notes = ""
            elif combo_parts:
                mapped_msku = f"COMBO::{raw_msku}"
                combo_flag = "Yes"
                notes = f"Contains: {', '.join(combo_parts)}"
            else:
                mapped_msku = "UNMAPPED"
                combo_flag = "Unknown"
                notes = "MSKU not found or combo not matched"
                self.log_unmapped(row['MSKU'])

            self.cleaned.append({
                "Date": row["Date"],
                "MSKU": mapped_msku,
                "Quantity": row["Quantity"],
                "Fulfillment Center": row["Fulfillment Center"],
                "Status": row["Disposition"],
                "Combo?": combo_flag,
                "Notes": notes
            })

    def log_unmapped(self, msku):
        with open(self.log_path, "a") as log_file:
            log_file.write(f"{msku}\n")

    def export(self, output_path):
        pd.DataFrame(self.cleaned).to_csv(output_path, index=False)
