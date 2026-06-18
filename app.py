import pandas as pd
import glob
import os

def auto_read_csv_file():
    print("🔄 Scanning folder for CSV files...")
    
    # 1. Automatically find all .csv files in the current folder
    csv_files = glob.glob("*.csv")
    
    # If no CSV file is found in the folder
    if not csv_files:
        print("❌ Error: No CSV file found in this folder! Please place your file here first.")
        return
        
    # 2. Select the first CSV file automatically
    selected_file = csv_files[0]
    print(f"✅ File found: '{selected_file}'")
    print("🔄 Loading data, please wait...")
    
    try:
        # 3. Read only the first 10 rows for a quick layout preview
        df = pd.read_csv(selected_file, nrows=10, low_memory=False)
        
        # 4. Smart Counting: Calculate total rows in chunks to prevent RAM crashes
        total_rows = 0
        for chunk in pd.read_csv(selected_file, chunksize=100000, low_memory=False):
            total_rows += len(chunk)
            
        print("\n" + "="*50)
        print("📊 FILE OVERVIEW (AUTOMATIC)")
        print("="*50)
        print(f"🔹 File Name : {selected_file}")
        print(f"🔹 Total Rows : {total_rows:,}")
        print(f"🔹 Total Columns : {len(df.columns)}")
        
        # 5. Display the data sample preview on the CMD screen
        print("\n👇 Data Preview (First 10 Rows):")
        print(df)
        
    except Exception as e:
        print(f"❌ An error occurred while opening the file: {str(e)}")

if __name__ == "__main__":
    auto_read_csv_file()
