import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
Fmean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
print(Fmean)

fig = px.scatter(df,x = "student_id",y ="level" ,color = "attempt")
fig.show()
