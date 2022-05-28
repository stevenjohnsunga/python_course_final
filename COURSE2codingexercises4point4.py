import pandas as pd

df = pd.read_csv("population_by_country_2020.csv")

east_asia = df[df["Country"].isin(["China","South Korea","North Korea","Macau","Hong Kong","Tibet","Taiwan","Mongolia"])]
east_asia.describe()

