## 2. The Mean as the Center ##

#List of values
values = [2, 4, 5, -1, 0, 10, 8, 9]
# Compute the mean of the values
values_mean = sum(values) / len(values)
# Find the difference between each of the values and the mean by subtracting the mean from each value.
differences = [i - values_mean for i in values]
# This equals 0.  If you'd like, try changing the values around to verify that it still equals 0.
print(sum(differences))
#import median function from numpy module
from numpy import median
values_median = numpy.median(values)
median_difference_sum = sum([i - values_median for i in values])
print(median_difference_sum)

## 3. Finding Variance ##

import matplotlib.pyplot as plt
import pandas as pd
# We've already loaded the NBA data into the nba_stats variable. Now, we look for the mean
pf_mean = nba_stats["pf"].mean()
# Initialize variable
variance = 0
# Loop through each item in the "pf" column.
for p in nba_stats["pf"]:
    # Calculate the difference between the mean and the value.
    difference = p - pf_mean
    # Square the difference. This ensures that the result isn't negative.
    # If we didn't square the difference, the total variance would be zero.
    # ** in python means "raise whatever comes before this to the power of whatever number is after this."
    square_difference = difference ** 2
    # Add the difference to the total.
    variance += square_difference
# Average the total to find the final variance.
variance = variance / len(nba_stats["pf"])


#Find the mean of the pts column in dataframe
pts_mean = nba_stats["pts"].mean()
#Initialize variance_pts for storing variance of points column
variance_pts = 0

#Loop to calculate variance
for i in nba_stats["pts"]:
    difference = i - pts_mean
    
    square_difference = difference**2
    variance_pts += square_difference
variance_pts = variance_pts /len(nba_stats["pts"])
point_variance = variance_pts

## 4. Understanding the Order of Operations ##

# You may be wondering why multiplication and division are on the same level.
# It doesn't matter whether we do the multiplication or division first; the answer here will always be the same.
# In this case, we need to think of division as multiplication by a fraction. Otherwise, we'll be dividing more than we want to.
# Create a formula
a = 5 * 5 / 2
# Multiply by 1/2 instead of dividing by 2. The result is the same (2/2 == 2 * 1/2).
a_subbed = 5 * 5 * 1/2
a_mul_first = 25 * 1/2
a_div_first = 5 * 2.5
print(a_mul_first == a_div_first)

# The same is true for subtraction and addition.
# In this case, we need to convert subtraction into adding a negative number. If we don't we'll end up subtracting more than we expect.
b = 10 - 8 + 5
# Add -8 instead of subtracting 8.
b_subbed = 10 + -8 + 5
b_sub_first = 2 + 5
b_add_first = 10 + -3
print(b_sub_first == b_add_first)

c = (5*10) / 2 
d = (3 - 1) / (2 * 2)

## 5. Using Parentheses to Change the Order of Operations ##

a = 50 * 50 - 10 / 5
a_paren = 50 * (50 - 10) / 5
# If we put multiple operations inside parentheses, the interpreter will use the order of operations to determine the sequence in which it should execute them.
a_paren = 50 * (50 - 10 / 5)
b = 10 * (10 + 100)
c = (8 - 6) * 100

## 6. Fractional Powers ##

a = 5 ** 2
# Raise to the fourth power
b = 10 ** 4

# Take the square root ( 3 * 3 == 9, so the answer is 3)
c = 9 ** (1/2)

# Take the cube root (4 * 4 * 4 == 64, so 4 is the cube root)
d = 64 ** (1/3)
e = 11**5
f = 10000**(1/4)

## 7. Calculating Standard Deviation ##

# We've already loaded the NBA stats into the nba_stats variable.
def std_dev(column):
    #Initialize the associated output variable "standard deviation"
    variance = 0
    std_deviation = 0
    
    length = len(column)
    
    mean = column.mean()

    difference = column - mean
    squared_difference = difference **2
    
    variance = sum(squared_difference)
    variance = variance / length
    
    std_deviation = variance ** (1/2)
    
    return (std_deviation)

mp_dev = std_dev(nba_stats["mp"])
ast_dev = std_dev(nba_stats["ast"])
print(mp_dev)
print(ast_dev)

## 8. Finding Standard Deviation Distance ##

import matplotlib.pyplot as plt

plt.hist(nba_stats["pf"])
mean = nba_stats["pf"].mean()
plt.axvline(mean, color="r")

std_dev = nba_stats["pf"].std()
# Plot a line one standard deviation below the mean.
plt.axvline(mean - std_dev, color="g")
# Plot a line one standard deviation above the mean.
plt.axvline(mean + std_dev, color="g")

# We can see how many of the data points fall within one standard deviation of the mean.
# The more that fall into this range, the more dense the data is.
plt.show()

# We can calculate how many standard deviations a data point is from the mean by doing some subtraction and division.
# First, we find the total distance by subtracting the mean.
total_distance = nba_stats["pf"][0] - mean
# Then we divide by standard deviation to find how many standard deviations away the point is.
standard_deviation_distance = total_distance / std_dev

point_10 = nba_stats["pf"][9]
point_100 = nba_stats["pf"][99]

total_dist_10 = point_10 - mean
point_10_std = total_dist_10 /  std_dev

total_dist_100 = point_100 - mean
point_100_std = total_dist_100 /  std_dev

## 9. Working with the Normal Distribution ##

import numpy as np
import matplotlib.pyplot as plt
# The norm module has a pdf function
from scipy.stats import norm

# The arange function generates a numpy vector
# The vector below will start at -1, and go up to, but not including 1
# It will proceed in "steps" of .01.
points = np.arange(-1, 1, 0.01)

# The norm.pdf function will take the points vector and convert it into a probability vector
# Each element in the vector will correspond to the normal distribution (earlier elements and later element smaller, peak in the center)
# The distribution will be centered on 0, and will have a standard devation of .3
probabilities = norm.pdf(points, 0, .3)

plt.plot(points, probabilities)
plt.show()


points_2 = np.arange(-10,10,0.1)

prob_2 = norm.pdf(points_2,0,2)

plt.plot(points_2,prob_2)
plt.show()

## 10. Normal Distribution Deviation ##

# Housefly wing lengths in millimeters
wing_lengths = [36, 37, 38, 38, 39, 39, 40, 40, 40, 40, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 42, 43, 43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 48, 49, 49, 49, 49, 49, 49, 49, 50, 50, 50, 50, 50, 50, 51, 51, 51, 51, 52, 52, 53, 53, 54, 55]

mean = sum(wing_lengths) / len(wing_lengths)

variances = [(val - mean)**2 for val in wing_lengths]
variance = sum(variances)/len(wing_lengths)
standard_deviation = variance **(1/2)

standard_deviations = [ (value -mean) / standard_deviation for value in wing_lengths]

def within_perc(deviations, count):
    within = [i for i in deviations if i <=count and i>= -count]
    count = len(within)
    return(count/len(deviations))

within_one_percentage = within_perc(standard_deviations, 1)
within_two_percentage = within_perc(standard_deviations, 2)
within_three_percentage = within_perc(standard_deviations, 3)

## 11. Using Scatterplots to Plot Correlations ##

import matplotlib.pyplot as plt

# Plot field goals attempted (number of shots someone takes in a season) vs. point scored in a season.
# Field goals attempted is on the x-axis, and points is on the y-axis.
# As you can tell, they are very strongly correlated. The plot is close to a straight line.
# The plot also slopes upward, which means that as field goal attempts go up, so do points.
# That means that the plot is positively correlated.
plt.scatter(nba_stats["fga"], nba_stats["pts"])
plt.show()

# If we make points negative (so the people who scored the most points now score the least, because 3000 becomes -3000), we can change the direction of the correlation.
# Field goals are negatively correlated with our new "negative" points column -- the more free throws you attempt, the less negative points you score.
# We can see this because the correlation line slopes downward.
plt.scatter(nba_stats["fga"], -nba_stats["pts"])
plt.show()

# Now, we can plot total rebounds (number of times someone got the ball back for their team after someone shot) vs total assists (number of times someone helped another person score).
# These are uncorrelated, so you don't see the same nice line as you see with the plot above.
plt.scatter(nba_stats["trb"], nba_stats["ast"])
plt.show()

plt.scatter(nba_stats["fta"], nba_stats["pts"])
plt.show()
plt.scatter(nba_stats["stl"], nba_stats["pf"])
plt.show()

## 12. Measuring Correlation with Pearson's r ##

from scipy.stats.stats import pearsonr

# The pearsonr function will find the correlation between two columns of data.
# It returns the r value and the p value.  We'll learn more about p values later on.
r, p_value = pearsonr(nba_stats["fga"], nba_stats["pts"])

print(r)

# These two columns are much less correlated.
r, p_value = pearsonr(nba_stats["trb"], nba_stats["ast"])
# We get a much lower, but still positive, r value.
print(r)


r_fta_pts, p_value = pearsonr(nba_stats["fta"], nba_stats["pts"])

print(r_fta_pts)



r_stl_pf, p_value = pearsonr(nba_stats["stl"], nba_stats["pf"])

print(r_stl_pf)

## 13. Calculate Covariance ##

# We've already loaded the nba_stats variable.

def covariance(X, Y):
    meanX = sum(X) / len(X)
    meanY = sum(Y) / len(Y)
    len_vect = len(X)
    
    varX = (X-meanX)**2
    variance_X = sum(varX) / len_vect
    
    varY = (Y-meanY)**2
    variance_Y = sum(varY) / len_vect
    
    cov = [(X[i] - meanX)*(Y[i] - meanY) for i in range(0,len(X))]
    covariance = sum(cov) / len_vect
    
    return(covariance)

cov_stl_pf =  covariance(nba_stats["stl"], nba_stats["pf"])
cov_fta_pts = covariance(nba_stats["fta"], nba_stats["pts"])

## 14. Calculate Correlation With the std() Method ##

from numpy import cov

r_fta_blk = cov(nba_stats["fta"], nba_stats["blk"])[0,1] / ((nba_stats["fta"].var() * nba_stats["blk"].var())** (1/2))
r_ast_stl = cov(nba_stats["ast"], nba_stats["stl"])[0,1] / ((nba_stats["ast"].var() * nba_stats["stl"].var())** (1/2))