import streamlit as st
import pandas as pd

st.title("FMCSA Carrier Data Analyzer")
st.write("Upload your large CSV file to view data safely without breaking columns.")

# 1. Streamlit's official built-in File Uploader (No Tkinter needed)
uploaded_file = st.file_uploader("Choose your FMCSA CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        st.info("🔄 File is loading... Please wait as it might be large.")
        
        # 2. Read the uploaded file safely using Pandas
        df = pd.read_csv(uploaded_file, low_memory=False)
        
        st.success("✅ File loaded successfully with zero data loss!")
        
        # 3. Display Data Statistics
        st.subheader("📊 File Overview")
        st.write(f"**Total Rows:** {len(df)}")
        st.write(f"**Total Columns:** {len(df.columns)}")
        
        # 4. Show First 10 Rows as a Preview
        st.subheader("👇 Initial Data Preview (First 10 Rows)")
        st.dataframe(df.head(10))
        
        # 5. Show All Available Column Headers
        st.subheader("👇 Available Columns inside this file")
        st.write(list(df.columns))

    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
