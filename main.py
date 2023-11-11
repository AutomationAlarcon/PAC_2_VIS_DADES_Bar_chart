import pandas as pd
import matplotlib.pyplot as plt


file_path = 'world_data_2023.csv'
df = pd.read_csv(file_path, sep=",", skipinitialspace=True)
df1 = df[["Country", "Life expectancy"]]
df1["Country"] = df1["Country"].astype("category")
df1["Life expectancy"] = df1["Life expectancy"].astype("float")
mean_value = df1["Life expectancy"].mean()
print("Global life expectancy mean value is {}".format(mean_value))
df1.sort_values(by="Life expectancy", ascending=False, inplace=True)

df2 = df1.iloc[:10]
df2.sort_values(by="Life expectancy", ascending=True, inplace=True)
print(df2.head(10))

plt.figure(figsize=(10,10))

bars = plt.barh(df2["Country"], df2["Life expectancy"], color='lightgray')
plt.title('The 10 countries with more life expectancy', fontsize=20)
plt.xlim(65, 88)
plt.xlabel('Life expectancy (Years)', fontsize=20)
plt.ylabel('Countries', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

for bar in bars:
    xval = bar.get_width()
    plt.text(xval + 0.05, bar.get_y() + bar.get_height() / 2, round(xval, 2), ha='left', va='center', fontsize=16)

plt.savefig("life_expectancy", dpi=100, bbox_inches='tight')
