import pandas as pd
import os #helps me navigate with my folders as had issues locating folders for the files and print(os.getcwd)) does magic!

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