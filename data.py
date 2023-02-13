import pandas as pd
import seaborn as sns
  
data = pd.read_csv("iris_csv.csv")

#print(data.head())
#print(data.sample(10))
#print(data.columns)
#print(data.shape)
#print(data)

#print(data[10:21])

#sliced_data=data[10:21]
#print(sliced_data)

#specific_data = data[["class"]]
#print(specific_data.head(10))
#print(data.iloc[5])
#print(data.loc[data["class"] == "Iris-setosa"])

#print(data["class"].value_counts())

#sum_data = data["sepallength"].sum()
#mean_data = data["sepallength"].mean()
#median_data = data["sepallength"].median()
#print("Sum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data)

#min_data=data["sepallength"].min()
#max_data=data["sepallength"].max()
#print("Minimum:",min_data, "\nMaximum:", max_data)

#cols = data.columns
#cols = cols[0:4]
#data1 = data[cols]
#data["total_values"]=data1[cols].sum(axis=1)
#print(data)
  

#newcols={"sepallength":"SepalLengthCm", "sepalwidth":"SepalWidthCm"}
#data.rename(columns=newcols,inplace=True)
#print(data.head())

#data.style

#data.head(10).style.highlight_max(color='lightgreen', axis=0)
#data.head(10).style.highlight_max(color='lightgreen', axis=1)
#data.head(10).style.highlight_max(color='lightgreen', axis=None)

#data.isnull

#data.isnull().sum()

#iris = sns.load_dataset("iris")
#sns.heatmap(iris.corr(), cmap = "YlGnBu", linecolor = 'white', linewidths = 1, annot = True)

#data.corr(method='pearson')

#g = sns.pairplot(data,hue="class")