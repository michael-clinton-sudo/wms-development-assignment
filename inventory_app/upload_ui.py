from flask import Flask, request, render_template, send_file
import pandas as pd
from data_cleaner import process_file
from nocodb_api import upload_to_nocodb
from ai_query import query_dataframe
import os

app = Flask(__name__)
UPLOAD_FOLDER = "cleaned_output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            cleaned_df = process_file(filepath)
            output_path = os.path.join(UPLOAD_FOLDER, "result.csv")
            cleaned_df.to_csv(output_path, index=False)
            upload_to_nocodb(cleaned_df)
            return render_template("index.html", table=cleaned_df.to_html(classes='data'), filename="result.csv")
    return render_template("index.html")

@app.route("/download/<filename>")
def download(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename), as_attachment=True)

@app.route("/query", methods=["POST"])
def handle_query():
    user_query = request.form["query"]
    data_path = os.path.join(UPLOAD_FOLDER, "result.csv")
    if not os.path.exists(data_path):
        return "Please upload a file first."

    df = pd.read_csv(data_path)
    result_df = query_dataframe(df, user_query)
    return render_template("index.html", table=result_df.to_html(classes='data'))

if __name__ == "__main__":
    app.run(debug=True)
