import seaborn as sns
df = sns.load_dataset('iris')
my_pal = {"versicolor": "g", "setosa": "b", "virginica":"m"}
sns.boxplot( x=df["species"], y=df["sepal_length"], palette=my_pal)
#sns.plt.show()
