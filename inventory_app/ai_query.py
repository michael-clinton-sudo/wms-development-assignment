import pandas as pd

def query_dataframe(df, user_query):
    query = user_query.strip().lower()

    # 1. List of supported queries
    if query == "list":
        questions = [
            "show all",
            "total quantity",
            "show tlcq",
            "total buffer stock",
            "total opening stock",
            "show products with zero stock",
            "list all unique MSKUs",
            "show products with missing fields",
            "total count of products",
            "list all column names"
        ]
        return pd.DataFrame({"Supported Queries": questions})

    # 2. Show all rows
    elif "show all" in query:
        return df

    # 3. Total quantity (dynamic column search)
    elif "total quantity" in query:
        quantity_col = next((col for col in df.columns if "quantity" in col.lower()), None)
        if quantity_col:
            return pd.DataFrame([{"Total Quantity": df[quantity_col].sum()}])
        return pd.DataFrame([{"Error": "No quantity column found."}])

    # 4. Total buffer stock
    elif "total buffer" in query:
        buffer_col = next((col for col in df.columns if "buffer" in col.lower()), None)
        if buffer_col:
            return pd.DataFrame([{"Total Buffer Stock": df[buffer_col].sum()}])
        return pd.DataFrame([{"Error": "No buffer column found."}])

    # 5. Total opening stock
    elif "total opening" in query:
        opening_col = next((col for col in df.columns if "opening" in col.lower()), None)
        if opening_col:
            return pd.DataFrame([{"Total Opening Stock": df[opening_col].sum()}])
        return pd.DataFrame([{"Error": "No opening stock column found."}])

    # 6. Show TLCQ
    elif "tlcq" in query:
        if "tlcq" in df.columns:
            return df[df["TLCQ"] > 0]
        else:
            tlcq_col = next((col for col in df.columns if "tlcq" in col.lower()), None)
            if tlcq_col:
                return df[df[tlcq_col] > 0]
        return pd.DataFrame([{"Error": "No TLCQ column found."}])

    # 7. Show products with zero stock
    elif "zero stock" in query:
        stock_col = next((col for col in df.columns if "stock" in col.lower()), None)
        if stock_col:
            return df[df[stock_col] == 0]
        return pd.DataFrame([{"Error": "No stock column found."}])

    # 8. Unique MSKUs
    elif "msku" in query and "unique" in query:
        msku_col = next((col for col in df.columns if "msku" in col.lower()), None)
        if msku_col:
            return pd.DataFrame(df[msku_col].dropna().unique(), columns=["Unique MSKUs"])
        return pd.DataFrame([{"Error": "No MSKU column found."}])

    # 9. Missing fields
    elif "missing" in query or "null" in query:
        return df[df.isnull().any(axis=1)]

    # 10. Count of products
    elif "total count" in query or "number of products" in query:
        return pd.DataFrame([{"Total Rows": len(df)}])

    # 11. Column names
    elif "column names" in query:
        return pd.DataFrame({"Column Names": df.columns})

    # 12. Default
    else:
        return pd.DataFrame([{"Message": "Query not understood. Type 'list' to see supported queries."}])
