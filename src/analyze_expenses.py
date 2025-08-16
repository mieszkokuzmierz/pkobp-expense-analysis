import pandas as pd
import os #helps me navigate with my folders as had issues locating folders for the files and print(os.getcwd)) does magic!
import matplotlib.pyplot as plt

df = pd.read_csv('../data/sample_data.csv') #reading .csv file to pandas

#Let’s start with some headers

print('Data preview:')
print(df.head(), '\n')
print('Columns:')
print(df.columns, '\n')

#Let's convert 'Kwota' colums to numbers with .to_numeric function from Pandas
df['Kwota'] = pd.to_numeric(df['Kwota'], errors = 'coerce')

#Let's separate incomes and expenses and sum them up
incomes = df[df['Kwota'] > 0]['Kwota'].sum()
expenses = df[df['Kwota'] < 0]['Kwota'].sum()

print(f'Sum of incomes: {incomes:.2f}')
print(f'Sum of expenses: {expenses:.2f}')
print(f'Balance: {incomes + expenses:.2f}')

#Let's add 10 biggest spending from the file
top_expenses = df[df['Kwota'] < 0].sort_values(by='Kwota').head(10).reset_index(drop = True)
print('Top 10 expenses:')
print(top_expenses[['Data operacji', 'Kwota', 'Opis transakcji']])

#Quick check to convert 'Data Operacji' to date (if not it will be change to NaT)
df['Data operacji'] = pd.to_datetime(df['Data operacji'], errors='coerce')

#Creates a table that shows how much was spent on particular date
daily_expenses = df[df['Kwota'] < 0].groupby(df['Data operacji'].dt.date)['Kwota'].sum()
daily_incomes = df[df['Kwota'] > 0].groupby(df['Data operacji'].dt.date)['Kwota'].sum()
daily_balance = df.groupby(df["Data operacji"].dt.date)["Kwota"].sum()

print('Daily expenses report: \n')
print(daily_expenses.head(10))
print('Daily incomes report: \n')
print(daily_incomes.head(10))
print('Daily balance report: \n')
print(daily_balance.head(10))

#Adding a chart showing sum od daily transactions
print('Sum of expenses and incomes on particlar days: ')
plt.figure(figsize=(10,5))
daily_balance.plot(kind="bar")
plt.title("Bilans dzienny")
plt.xlabel("Data")
plt.ylabel("Kwota [PLN]")
plt.xticks(rotation=45)
plt.show()