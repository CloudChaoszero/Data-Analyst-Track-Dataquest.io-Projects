## 3. Finding Correlations With the r Value ##

correlations = combined.corr()
correlations = correlations["sat_score"]
print(correlations)

## 5. Plotting Enrollment With the Plot() Accessor ##

import matplotlib.pyplot as plt
combined.plot.scatter(x="total_enrollment",y="sat_score")

## 6. Exploring Schools With Low SAT Scores and Enrollment ##

low_enrollment = combined[combined["total_enrollment"] < 1000]
low_enrollment = low_enrollment[low_enrollment["sat_score"] < 1000]
print(low_enrollment["School Name"])

## 7. Plotting Language Learning Percentage ##

combined.plot.scatter(x='ell_percent', y='sat_score')
plt.show()

## 9. Mapping the Schools With Basemap ##

#We need to convert the pandas series containing the latitude and longitude coordinates to lists using #pandas.Series.tolist()method

#We then make a scatterplot using the long and lat with scatter() method on the Basemap object
#s is the size of point, zorder =2, and latlon is a boolean

#Then show the plot using the pyplot.show() method

from mpl_toolkits.basemap import Basemap
m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

longitudes = combined["lon"].tolist()
latitudes = combined["lat"].tolist()

m.scatter(x=longitudes, y = latitudes, zorder = 2, s=20, latlon=True)
plt.show()

## 10. Plotting Out Statistics ##

from mpl_toolkits.basemap import Basemap

m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

longitudes = combined["lon"].tolist()
latitudes = combined["lat"].tolist()
m.scatter(longitudes, latitudes, s=20, zorder=2, latlon=True, c=combined["ell_percent"], cmap="summer")
plt.show()

## 11. Calculating District-Level Statistics ##

import numpy as np
combined_school_dist = combined.groupby("school_dist")
districts = combined_school_dist.agg(np.mean)
districts.reset_index(inplace = True)
print(districts)

## 12. Plotting Percent Of English Learners by District ##

from mpl_toolkits.basemap import Basemap
#Create instance of Basemap
m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)
#Draw map boundary
m.drawmapboundary(fill_color='#85A6D9')
#Draw Coastlines
m.drawcoastlines(color='#6D5F47', linewidth=.4)
#Draw Rivers
m.drawrivers(color='#6D5F47', linewidth=.4)

#Create Longitude and Latitude lists from Districts Dataframe
longitudes = districts["lon"].tolist()
latitudes = districts["lat"].tolist()

m.scatter(x = longitudes, y = latitudes, s= 50, zorder = 2, latlon=True, c =districts["ell_percent"], cmap= "summer")
plt.show()