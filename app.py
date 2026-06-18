import pandas as pd
import glob

def show_just_two_rows():
    print("🔄 Finding your CSV file...")
    csv_files = glob.glob("*.csv")
    
    if not csv_files:
        print("❌ Error: No CSV file found in this folder!")
        return
        
    file_name = csv_files[0]
    print(f"✅ Opening: {file_name}")
    
    try:
        # Read exactly 2 rows + 1 header row
        df = pd.read_csv(file_name, nrows=2, low_memory=False)
        
        print("\n" + "="*60)
        print("📸 FILE IMAGE PREVIEW (1 Header + 2 Rows)")
        print("="*60)
        print(df.to_string())
        print("="*60)
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    show_just_two_rows()
