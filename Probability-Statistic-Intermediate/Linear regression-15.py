## 2. Drawing lines ##

import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 3, 4, 5]
# Going by our formula, every y value at a position is the same as the x-value in the same position.
# We could write y = x, but let's write them all out to make this more clear.
y = [0, 1, 2, 3, 4, 5]

# As you can see, this is a straight line that passes through the points (0,0), (1,1), (2,2), and so on.
plt.plot(x, y)
plt.show()

# Let's try a slightly more ambitious line.
# What if we did y = x + 1?
# We'll make x an array now, so we can add 1 to every element more easily.
x = np.asarray([0, 1, 2, 3, 4, 5])
y = x + 1

# y is the same as x, but every element has 1 added to it.
print(y)

# This plot passes through (0,1), (1,2), and so on.
# It's the same line as before, but shifted up 1 on the y-axis.
plt.plot(x, y)
plt.show()

y = x - 1
plt.plot(x,y)
plt.show()
y = x + 10
plt.plot(x,y)
plt.show()

## 3. Working with slope ##

import matplotlib.pyplot as plt
import numpy as np

x = np.asarray([0, 1, 2, 3, 4, 5])
# Let's set the slope of the line to 2.
y = 2 * x

plt.plot(x, y)
plt.show()

y = 4*x

plt.plot(x,y)
plt.show()

y = .5 * x
plt.plot(x,y)
plt.show()

y = -2 * x
plt.plot(x,y)
plt.show()

## 4. Starting out with linear regression ##

# The wine quality data is loaded into wine_quality
from numpy import cov
slope_density = cov(wine_quality["density"], wine_quality["quality"]) / wine_quality["density"].var()
print(slope_density[0][1])

## 5. Finishing linear regression ##

from numpy import cov

# This function will take in two columns of data, and return the slope of the linear regression line.
def calc_slope(x, y):
  return cov(x, y)[0, 1] / x.var()
intercept_density = wine_quality["quality"].mean() - (calc_slope(wine_quality["density"], wine_quality["quality"]) * wine_quality["density"].mean())

## 6. Making predictions ##

from numpy import cov

def calc_slope(x, y):
  return cov(x, y)[0, 1] / x.var()

# Calculate the intercept given the x column, y column, and the slope
def calc_intercept(x, y, slope):
  return y.mean() - (slope * x.mean())
slope = calc_slope(wine_quality["density"], wine_quality["quality"])
intercept = calc_intercept(wine_quality["density"], wine_quality["quality"], slope)

def compute_predicted_y(x):
  return x * slope + intercept

predicted_quality = wine_quality["density"].apply(compute_predicted_y)

## 7. Finding error ##

from scipy.stats import linregress


#Tuple unpack
slope, intercept, r_value, p_value, stderr_slope = linregress(wine_quality["density"], wine_quality["quality"])


# As you can see, these are the same values we calculated (except for slight rounding differences)
print(slope)
print(intercept)

import numpy
predicted_y = numpy.asarray([(slope * x) + intercept for x in wine_quality["density"]])
residuals = sum((wine_quality["quality"] - predicted_y)**2)
rss= residuals
print(rss)




## 8. Standard error ##

from scipy.stats import linregress
import numpy as np

# We can do our linear regression
# Sadly, the stderr_slope isn't the standard error, but it is the standard error of the slope fitting only
# We'll need to calculate the standard error of the equation ourselves
slope, intercept, r_value, p_value, stderr_slope = linregress(wine_quality["density"], wine_quality["quality"])

predicted_y = np.asarray([slope * x + intercept for x in wine_quality["density"]])
residuals = (wine_quality["quality"] - predicted_y) ** 2
rss = sum(residuals)
stand_error = (rss/(len(wine_quality["density"]-2))) **(1/2)

def within_perc(y, predicted_y, stderr, error_count):
    within = stderr * error_count
    
    differences = abs(predicted_y - y)
    
    
    ls_of_Ywithin = [i for i in differences if (i <=within)]
    within_count = len(ls_of_Ywithin)
    within_percentage = within_count / len(y)
    return(within_percentage)


within_one = within_perc(wine_quality["quality"],predicted_y, stand_error,1)
within_two = within_perc(wine_quality["quality"],predicted_y, stand_error,2)
within_three = within_perc(wine_quality["quality"],predicted_y, stand_error,3)