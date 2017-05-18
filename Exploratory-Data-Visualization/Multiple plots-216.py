## 1. Recap ##

import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])

x = unrate[0:12]["DATE"]
y = unrate[0:12]["VALUE"]
plt.plot(x,y)
plt.xticks(rotation = 90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()

## 3. Matplotlib Classes ##

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()

## 5. Adding Data ##

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

x1 = unrate[0:12]["DATE"]
y1 = unrate[0:12]["VALUE"]
ax1.plot(x1,y1)

x2 = unrate[12:24]["DATE"]
y2 = unrate[12:24]["VALUE"]
ax2.plot(x2,y2)
plt.show()

## 6. Formatting And Spacing ##

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()

## 7. Comparing Across More Years ##

#Method 1
'''
fig = plt.figure(figsize= (12,12))

ax1 = fig.add_subplot(5,1,1)
ax2 = fig.add_subplot(5,1,2)
ax3 = fig.add_subplot(5,1,3)
ax4 = fig.add_subplot(5,1,4)
ax5 = fig.add_subplot(5,1,5)
#1948
ax1.plot(unrate[0:12]["DATE"],unrate[0:12]["VALUE"])
#1949
ax2.plot(unrate[12:24]["DATE"],unrate[12:24]["VALUE"])
#1950
ax3.plot(unrate[24:36]["DATE"],unrate[24:36]["VALUE"])
#1951
ax4.plot(unrate[36:48]["DATE"],unrate[36:48]["VALUE"])
#1952
ax5.plot(unrate[48:60]["DATE"],unrate[48:60]["VALUE"])
plt.show()

'''
#Method 2
fig = plt.figure(figsize=(12,12))
for i in range(0,5):
    start = (i) * 12
    end = (i+1) * 12
    ax = fig.add_subplot(5,1,i+1)
    ax.plot(unrate[start:end]["DATE"], unrate[start:end]["VALUE"])
plt.show()

## 8. Overlaying Line Charts ##

unrate['MONTH'] = unrate['DATE'].dt.month
fig = plt.figure(figsize=(6,3))
plt.plot(unrate[0:12]['MONTH'],unrate[0:12]["VALUE"], c='red')
plt.plot(unrate[12:24]['MONTH'],unrate[12:24]["VALUE"], c='blue')
plt.show()

## 9. Adding More Lines ##

colors =  ["red","blue","green","orange","black"]
fig = plt.figure(figsize=(10,6))
for i in range(0,len(colors)):
    start = i * 12
    end = (i+1) * 12
    plt.plot(unrate[start:end]["MONTH"], unrate[start:end]["VALUE"], c = colors[i])
plt.show()

## 10. Adding A Legend ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i])
plt.show()

## 11. Final Tweaks ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')

plt.show()