
import pandas as pd

columns_list = ["Names","Price","P/E ratio", "PEG ratio", "Market Cap (B)","Analists Review","52-Week Range","Sector"]
df2 = pd.read_csv('Random Stocks Df.csv')
limit = df2.shape[1]-1  # shape - tuple with the first value on the x axis [0] and the second the y axis [1]

for i in range(0, df2.shape[1]):  # Code to know the dtypes of each column
    if i >= limit:
        pass
    else:
        print(columns_list[i]," :  ", df2.dtypes[i])


pe_mean = df2["P/E ratio"].mean()  # Gets the P/E mean
df2['PEG ratio'] = pd.to_numeric(df2['PEG ratio'])  # Converts "object" PEG ratio's dytpe to float. 
df2 = df2.loc[df2['PEG ratio']<50]  # Selects only good PEG ratio stocks (good growth)
df2 = df2.loc[df2['Analists Review']!="Sell"]  # It removes stocks with "sell" from the analists review
df2 = df2.loc[df2['Analists Review']!="Underperform"]  # It removes stocks with "underperform" from the analists review
df2 = df2.loc[df2['P/E ratio']<pe_mean]   # Gets the P/E below the mean; The P/E is better as it gets lower,
                                          # because indicates good earnings proportional to the size of the company

df2.to_csv('Selected Stocks Df.csv', index=True)  # Saves the selected stocks as csv

df_excel = pd.read_csv('Selected Stocks Df.csv')
GFG = pd.ExcelWriter("Selected Stocks Df.xlsx")
df_excel.to_excel(GFG, index=True)
GFG.save()

print(df2)
print("\n")
