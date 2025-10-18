import pandas as pd

# print(pd.__version__)

# Series 

data = [100, 102, 104, 200, 204]
series = pd.Series(data, index=["a", "b", "c", "d", "e"])

series.loc["e"] = 202

# print(series[series < 200])
# print(series.loc["a"]) # Location of this entry
# print(series.iloc[0]) # Location of this index (index 0 in this case)

calories = {"Day 1": 1750, "Day 2":2100, "Day 3":1700}

series = pd.Series(calories)

series.loc["Day 3"] += 500

# print(series.loc["Day 3"])
# print(series[series >= 2000])

# DataFrames

data = {"Name": ["Spongebob", "Patrick", "Squidward"],
        "Age": [20,25,50]
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

# print(df)

# print(df.loc["Employee 1"])
# print(df.iloc[0])

# Add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]

# print(df)

# Add a new row
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"}, {"Name": "Eugene", "Age": 60, "Job": "Manager"}], 
                       index=["Employee 4", "Employee 5"])
df = pd.concat([df, new_row])
# print(df)

# Importing

df = pd.read_csv("data.csv", index_col="Name")
# print(df.to_string()) # .to_string() prints entire df

# Selection

# print(df[["Name", "Height", "Weight"]].to_string())

# print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])
# print(df.iloc[0:11:2, 0:3])

# Filtering

tall_pokemon = df[df["Height"] >= 2]
heavy_pokemon = df[df["Weight"] > 100]

ff_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
# print(ff_pokemon)

# Aggregation

# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())

group = df.groupby("Type1")
# print(group["Height"].mean())

# Data Cleaning

# df = df.drop(columns=["Legendary", "No"])
# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2": "None"})

# print(df.to_string())

df["Type1"] = df["Type1"].replace({"Grass": "GRASS"})

# print(df)

df["Legendary"] = df["Legendary"].astype(bool)
# print(df)

df = df.drop_duplicates()