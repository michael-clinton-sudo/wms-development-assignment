
import pandas as pd

class SKUMapper:
    def __init__(self, mapping_path):
        self.mapping_df = pd.read_csv(mapping_path)
        self.mapping_dict = dict(zip(self.mapping_df['sku'], self.mapping_df['msku']))

    def map_sku(self, sku):
        return self.mapping_dict.get(sku, None)
