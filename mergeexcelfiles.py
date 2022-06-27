## Merge Multiple excel files
import os
import pandas as pd

# 1. defines path to excel files
try: 
    path = input("Enter the path to the csv files in the format: /Users/lazarinastoy/something/something/")
except EOFError:
        print("Input is empty")

# 2. creates list with excel files to merge based on name convention
file_list = [path + f for f in os.listdir(path) if f.endswith('.xlsx')]

# 3. creates empty list to include the content of each file converted to pandas DF
excel_list = []

# 4. reads each (sorted) file in file_list, converts it to pandas DF and appends it to the excel_list
for file in sorted(file_list):
    excel_list.append(pd.read_excel(file).assign(File_Name = os.path.basename(file)))
    
# 5. merges single pandas DFs into a single DF, index is refreshed 
excel_merged = pd.concat(excel_list, ignore_index=True)
 
# 6. Single DF is saved to the path in Excel format, without index column
excel_merged.to_excel(path + 'excel_files_combines.xlsx', index=False)