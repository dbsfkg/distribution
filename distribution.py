import plotly.figure_factory as ff 
import pandas as pd 
import csv 

df=pd.read_csv("data(5).csv")
fig=ff.create_distplot([df["AvgRating"].tolist()],["Average Rating"],show_hist=False)
fig.show()