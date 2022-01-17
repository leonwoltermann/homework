import os
import re
from pprint import pprint
import pandas
import numpy
import matplotlib.pyplot as plt
import plotly.express as px

dispatchFile = "entities.csv"
dispatch = pandas.read_csv(dispatchFile, sep="\t", header=0)

dispatch["month"] = [re.sub("-\d\d$", "-01", str(i)) for i in dispatch["date"]]
# convert into date format
dispatch["month"] = pandas.to_datetime(dispatch["month"], format="%Y-%m-%d")
dispatch["date"] = pandas.to_datetime(dispatch["date"], format="%Y-%m-%d")

# reorder columns
dispatch = dispatch[["itemID", "month", "date", "itemType", "itemUnified", "itemId"]]

dispatch_place = dispatch[dispatch["itemType"] == "placename"]

dispatch_place[["month", "itemId", "itemID"]]

tgnFile = "TGNOut_Coordinates.csv"
tgnData = pandas.read_csv(tgnFile, sep="\t", header=0)

tgnData.columns = ["itemId", "lat", "lon"]

merged = pandas.merge(dispatch_place, tgnData, on=["itemId"])

dispatchTextFile = "textList.csv"
dispatchText = pandas.read_csv(dispatchTextFile, sep="\t", header=0)
dispatchText = dispatchText[["itemID", "text"]]
place_text = pandas.merge(merged, dispatchText, on=["itemID"])

place_text = place_text[["month", "itemUnified", "itemId", "lat", "lon", "text"]]
place_text = place_text.sort_values('month')
place_text = place_text.reset_index()

var = "sherman"

dispatch_search = place_text[place_text["text"].str.contains(var)]
dispatch_search = dispatch_search.reset_index()
dispatch_search['occur'] = dispatch_search["text"].str.count(var)

sherman_place = dispatch_search[dispatch_search["occur"] > 3]

sherman_place = sherman_place[["month", "itemUnified", "lat", "lon"]]
sherman_place = sherman_place.reset_index()
sherman_place = sherman_place[["month", "itemUnified", "lat", "lon"]]

sherman_place = sherman_place.groupby(sherman_place.columns.tolist(),as_index=False).size()

sherman_place['month'] = sherman_place['month'].dt.strftime('%Y-%m')

'''
MAP
'''

# plot places
placesAll = sherman_place[['month', 'itemUnified','lat', 'lon', 'size']]
print(placesAll)

fig = px.scatter_geo(placesAll, lon='lon',lat='lat',hover_name="itemUnified",animation_frame="month",size='size')

fig.update_layout(
    title_text='Sherman Cities',
    showlegend=True,
    geo=dict(
        scope='usa',
        landcolor='rgb(235, 235, 235)',
    )
)

fig.show()
fig.write_html("sherman_cities.html")