import pandas
df = pandas.read_csv("data.csv")

new_df = df.fillna(
{"name": "saipal",
"marks": 92

}

)
print (new_df)
