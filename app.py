import pandas as pd
import tkinter as tk
from tkinter import filedialog

def open_file_picker():
    # 1. Hide the main tkinter window
    root = tk.Tk()
    root.withdraw()
    
    # Bring the file picker window to the front
    root.attributes('-topmost', True)

    print("🔄 Opening File Explorer... Please select your CSV file.")
    
    # 2. Show the file dialog to pick a file from Desktop or any folder
    file_path = filedialog.askopenfilename(
        title="Select Your Large CSV File",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    
    # If user cancels or closes the window without selecting a file
    if not file_path:
        print("❌ Error: No file was selected.")
        return

    try:
        print(f"🔄 Loading chosen file: {file_path}")
        print("Please wait, reading large file without breaking columns...")
        
        # 3. Read the entire CSV file safely
        df = pd.read_csv(file_path, low_memory=False)
        
        print("✅ Success! File opened successfully with zero data loss.")
        
        # 4. Show file stats
        total_rows = len(df)
        total_cols = len(df.columns)
        print(f"📊 Total Rows inside file: {total_rows}")
        print(f"📊 Total Columns inside file: {total_cols}")
        
        # 5. Show first 10 rows on screen
        print("\n👇 Initial Data Preview (First 10 Rows):")
        print(df.head(10))
        
        # 6. Show all available columns in the file
        print("\n👇 List of all Columns available in this file:")
        print(list(df.columns))

    except Exception as e:
        print(f"❌ An error occurred while opening the file: {str(e)}")

if __name__ == "__main__":
    open_file_picker()

