import xlrd
import pandas as pd

df = pd.read_excel(r'test02.xlsx', sheet_name='Sheet1')
print(df)

