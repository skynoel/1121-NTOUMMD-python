import pandas as pd
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度
df=pd.read_excel("import02.xlsx", sheet_name="工作表1")
print(df)
