import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

Food_Insecurity_filepath = "Maui_Food_Insecurity_Index.csv"
Food_Insecurity_data = pd.read_csv(Food_Insecurity_filepath, index_col=("County"), parse_dates=(True))
print(Food_Insecurity_data)
plt.figure(figsize=(10,10))
plt.title("Food Insecurity")
sns.barplot(x=Food_Insecurity_data.index, y=Food_Insecurity_data['Index value'])
plt.ylabel("Index value")
