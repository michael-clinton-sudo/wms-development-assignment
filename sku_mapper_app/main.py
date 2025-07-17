
from src.mapper import SKUMapper
from src.combo_handler import ComboHandler
from src.data_cleaner import SalesDataCleaner

def main():
    sales_file = "data/sales_data.csv"
    sku_mapping = "data/sku_to_msku_mapping.csv"
    combo_file = "data/combo_mapping.csv"
    output_file = "output/cleaned_sales_data.csv"
    log_file = "logs/unmapped_skus.log"

    mapper = SKUMapper(sku_mapping)
    combo = ComboHandler(combo_file)
    cleaner = SalesDataCleaner(sales_file, mapper, combo, log_file)

    cleaner.process()
    cleaner.export(output_file)
    print("✅ Cleaned data exported.")

if __name__ == "__main__":
    main()
