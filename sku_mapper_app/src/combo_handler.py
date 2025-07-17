
import pandas as pd

class ComboHandler:
    def __init__(self, combo_path):
        self.combo_df = pd.read_csv(combo_path)

    def get_combo_components(self, combo_sku):
        combo_row = self.combo_df[self.combo_df['Combo'] == combo_sku]
        if combo_row.empty:
            return []
        return [sku for sku in combo_row.values[0][1:] if pd.notna(sku)]
