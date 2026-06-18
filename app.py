import pandas as pd
import glob

def show_just_two_rows():
    print("🔄 Finding your CSV file in the folder...")
    csv_files = glob.glob("*.csv")
    
    if not csv_files:
        print("❌ Error: No CSV file found in this folder! Please copy your file here.")
        return
        
    file_name = csv_files[0]
    print(f"✅ Target File Detected: {file_name}")
    print("🔄 Fetching instant preview (1 Header + 2 Rows)...")
    
    try:
        # Crucial: Read exactly 2 rows so your PC never goes into thinking mode
        df = pd.read_csv(file_name, nrows=2, low_memory=False)
        
        print("\n" + "="*70)
        print("📸 INSTANT FILE IMAGE PREVIEW")
        print("="*70)
        print(df.to_string(index=False)) # Prints data cleanly inside CMD
        print("="*70)
        print("🎉 Successfully displayed without any lag or crash!")
        
    except Exception as e:
        print(f"❌ Error while reading file: {str(e)}")

if __name__ == "__main__":
    show_just_two_rows()
