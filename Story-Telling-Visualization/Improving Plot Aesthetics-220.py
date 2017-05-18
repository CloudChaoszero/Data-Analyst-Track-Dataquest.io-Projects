## 3. Introduction To The Data ##

import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
x = "Year"
y = "Biology"
plt.plot(women_degrees[x],women_degrees[y])
plt.show()

## 4. Visualizing The Gender Gap ##

x = women_degrees["Year"]
y_women = women_degrees["Biology"]

men_bio = 100- women_degrees["Biology"]
y_men = men_bio

plt.plot(x,y_women,c='blue',label = "Women")
plt.plot(x, y_men, c = 'green',label = "Men")
plt.legend(loc = "upper right")
plt.title("Percentage of Biology Degrees Awarded By Gender")
plt.show()

## 6. Hiding Tick Marks ##

x = women_degrees["Year"]
y_women = women_degrees["Biology"]
y_men = 100 - women_degrees["Biology"]

plt.plot(x,y_women, label = "Women")
plt.plot(x,y_men, label = "Men")

plt.title("Percentage of Biology Degrees Awarded By Gender")
plt.legend(loc = "upper right")
plt.tick_params(bottom = "off",top = "off", right = "off", left = "off")
plt.show()

## 7. Hiding Spines ##

fig, ax = plt.subplots()
ax.plot(women_degrees['Year'], women_degrees['Biology'], label='Women')
ax.plot(women_degrees['Year'], 100-women_degrees['Biology'], label='Men')
ax.tick_params(bottom="off", top="off", left="off", right="off")
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["top"].set_visible(False)

ax.legend(loc='upper right')
ax.set_title('Percentage of Biology Degrees Awarded By Gender')
plt.show()

## 8. Comparing Gender Gap Across Degree Categories ##

major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize = (25,25))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'],women_degrees[major_cats[sp]], c ="blue" ,label = "Women")
    ax.plot(women_degrees['Year'], 100 - women_degrees[major_cats[sp]], c = 'green', label = "Men")

    for key, spine in ax.spines.items():
        spine.set_visible(False)
       
    ax.set_title(major_cats[sp])
    ax.set_xlim(1968,2011)
    ax.set_ylim(0,100)
    ax.tick_params(bottom="off", top="off", left="off", right="off")                                 
plt.legend(loc = 'upper right')
plt.show()                          