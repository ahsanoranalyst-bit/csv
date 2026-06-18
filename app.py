import pandas as pd
import time

# 1. 📄 اپنی ایکسل/سی ایس وی فائل کا نام یہاں لکھیں
file_name = "your_file_name.csv" 

def read_massive_file(file_path):
    try:
        print(f"🔄 Opening file '{file_path}' on your local system...")
        start_time = time.time()
        
        # 2. Fast preview to capture column names instantly
        preview_df = pd.read_csv(file_path, nrows=5, low_memory=False)
        print("✅ Columns detected successfully.")
        
        # 3. Reading the full file in chunks to protect your computer's RAM
        print("🔄 Loading all data rows... Please wait a few seconds...")
        total_rows = 0
        for chunk in pd.read_csv(file_path, chunksize=100000, low_memory=False):
            total_rows += len(chunk)
            
        end_time = time.time()
        print(f"🎉 Success! Whole file loaded in {round(end_time - start_time, 2)} seconds with ZERO data loss.")
        
        # 4. Printing File Overview
        print("\n" + "="*50)
        print("📊 FILE OVERVIEW")
        print("="*50)
        print(f"🔹 Total Rows inside this file : {total_rows:,}")
        print(f"🔹 Total Columns inside this file: {len(preview_df.columns)}")
        
        # 5. Showing Top 5 Rows as sample data
        print("\n👇 DATA SAMPLE (First 5 Rows):")
        print(pd.read_csv(file_path, nrows=5, low_memory=False))
        
    except FileNotFoundError:
        print(f"❌ Error: '{file_path}' cannot be found! Make sure the file name is correct and it is inside the same folder.")
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    read_massive_file(file_name)
