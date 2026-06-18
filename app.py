import streamlit as st
import pandas as pd

st.set_page_config(page_title="FMCSA Data Analyzer", layout="wide")
st.title("🚀 All-in-One FMCSA Carrier Data Analyzer")
st.write("Upload any file (Small or Large up to 3GB) safely without system crash.")

# Streamlit Universal File Uploader
uploaded_file = st.file_uploader("Choose your FMCSA CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        st.info("🔄 Processing file... Please wait.")
        
        # 1. Read only first 100 rows for lightning-fast Preview and Columns detection
        preview_df = pd.read_csv(uploaded_file, nrows=100, low_memory=False)
        
        st.success("✅ File connected successfully!")
        
        # Reset file pointer to read total length safely
        uploaded_file.seek(0)
        
        # 2. Smart Counting: Calculate total rows in chunks so Large Files don't crash RAM
        total_rows = 0
        for chunk in pd.read_csv(uploaded_file, chunksize=100000, low_memory=False):
            total_rows += len(chunk)
            
        # Display File Information
        st.subheader("📊 File Overview")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Rows Found", f"{total_rows:,}")
        with col2:
            st.metric("Total Columns Found", len(preview_df.columns))
        
        # 3. Show Preview of Data
        st.subheader("👇 Data Preview (First 10 Rows)")
        st.dataframe(preview_df.head(10))
        
        # 4. Show All Available Column Names
        st.subheader("👇 Available Columns inside this file")
        st.write(list(preview_df.columns))

    except Exception as e:
        st.error(f"❌ An error occurred while reading the file: {str(e)}")
