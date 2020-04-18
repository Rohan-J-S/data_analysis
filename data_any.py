import pandas
df = pandas.read_csv("mar.csv",header=None,names = ["name","marks","IQ","codmaxkills"],nrows = 4)

print(df)
df.to_csv("new.csv",columns=["name","marks"])
