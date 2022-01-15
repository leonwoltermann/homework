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

dispatch_place[["month", "itemId"]]

tgnFile = "TGNOut_Coordinates.csv"
tgnData = pandas.read_csv(tgnFile, sep="\t", header=0)

tgnData.columns = ["itemId", "lat", "lon"]

merged = pandas.merge(dispatch_place, tgnData, on=["itemId"])

merged = merged[["itemUnified","month","lat","lon"]]

merged = merged.sort_values('month')

merged = merged.reset_index()

merged = merged[["month","itemUnified","lat","lon"]]
merged = merged.groupby(merged.columns.tolist(),as_index=False).size()

merged['month'] = merged['month'].dt.strftime('%Y-%m')




'''
MAP
'''

# plot places
placesAll = merged[['month', 'itemUnified', 'size', 'lat', 'lon']]
print(placesAll)

fig = px.scatter_geo(placesAll, lon='lon',lat='lat',hover_name="itemUnified",animation_frame="month",size='size')

fig.update_layout(
    title_text='Growth of US cities (1790-2010)',
    showlegend=True,
    geo=dict(
        scope='usa',
        landcolor='rgb(235, 235, 235)',
    )
)

fig.show()
fig.write_html("dispatch_cities.html")


