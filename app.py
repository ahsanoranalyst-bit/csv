import pandas as pd
import glob

def play_local_file():
    print("🔄 Scanning folder for your CSV file...")
    
    # Automatically find any CSV file in the same folder
    csv_files = glob.glob("*.csv")
    
    if not csv_files:
        print("❌ Error: No CSV file found in this folder! Put your file here.")
        return
        
    selected_file = csv_files[0]
    print(f"✅ Found file: '{selected_file}'")
    print("🔄 Opening file instantly (RAM Safe Mode)...")
    
    try:
        # Crucial Part: Read ONLY 10 rows so your PC never freezes or hangs
        df = pd.read_csv(selected_file, nrows=10, low_memory=False)
        
        print("\n" + "="*50)
        print("📊 DATA PREVIEW (SUCCESS)")
        print("="*50)
        print(f"🔹 File Name: {selected_file}")
        print(f"🔹 Total Columns Detected: {len(df.columns)}\n")
        
        # Display the actual data right inside your CMD
        print(df)
        print("="*50)
        
    except Exception as e:
        print(f"❌ Error opening file: {str(e)}")

if __name__ == "__main__":
    play_local_file()
