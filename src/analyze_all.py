import pandas as pd
import glob
import os

# finds all .csv files in data/ folder
files = glob.glob(os.path.join('../data/*.csv'))

dfs = []
for file in files:
    df = pd.read_csv(file)
    # upewnijmy się, że kolumna Kwota jest liczbą
    df['Kwota'] = pd.to_numeric(df['Kwota'], errors="coerce") #making sure 'Kwota' value is a number
    dfs.append(df)

# appending all files into one data frame
all_data = pd.concat(dfs, ignore_index=True)

# adding month column in format: YYYY-MM
all_data['Miesiąc'] = pd.to_datetime(all_data['Data operacji']).dt.to_period('M')
monthly_summary = all_data.groupby('Miesiąc')['Kwota'].sum()

print('=== Monthly Summary: ===')
print(monthly_summary)

# save file to .csv
monthly_summary.to_csv('monthly_summary.csv', header=['Saldo'])
