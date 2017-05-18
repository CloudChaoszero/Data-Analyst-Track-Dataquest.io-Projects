## 3. Introduction To The Data ##

import pandas as pd
unrate = pd.read_csv("unrate.csv")
unrate["DATE"] =  pd.to_datetime(unrate["DATE"])
print(unrate.iloc[:12]["DATE"])

## 7. Introduction to Matplotlib ##

import matplotlib.pyplot as plt
plt.plot()
plt.show()

## 8. Adding Data ##

x = unrate.iloc[:12]["DATE"]
y = unrate.iloc[:12]["VALUE"]
plt.plot(x,y)
plt.show()

## 9. Fixing Axis Ticks ##

x= unrate[0:12]["DATE"]
y = unrate[0:12]["VALUE"]
plt.plot(x,y)
plt.xticks(rotation = 90)
plt.show()

## 10. Adding Axis Labels And A Title ##

x = unrate[0:12]["DATE"]
y = unrate[0:12]["VALUE"]
plt.plot(x,y)
plt.xticks(rotation = 90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()
