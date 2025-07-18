
# Inventory Mapping App

## 📦 Features
- Upload CSV/Excel file
- Clean and map SKUs → MSKUs
- Handle combo products
- Upload to NocoDB
- Export cleaned data

## ▶️ Run Instructions
1. Install dependencies:
```bash
pip install flask pandas openpyxl requests
```

2. Run the app:
```bash
python upload_ui.py
```

3. Visit `http://localhost:5000` in your browser.

4. Upload your raw Excel or CSV file.

5. Preview data and download cleaned CSV or push to NocoDB.

## 📁 Folder Structure
- `upload_ui.py`: Flask frontend
- `data_cleaner.py`: Cleans and maps data
- `nocodb_api.py`: Uploads to NocoDB
- `templates/`: HTML UI
- `sample_data/`: SKU and combo sample CSVs

## 🔗 NocoDB
Update your API key and endpoint in `nocodb_api.py`.
