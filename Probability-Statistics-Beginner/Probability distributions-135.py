## 3. Bikesharing distribution ##

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")
print(bikes.shape)

more_than_5000_riders = bikes[bikes["cnt"] >5000].shape[0]
total_count = bikes.shape[0]

prob_over_5000 = more_than_5000_riders /total_count
print(prob_over_5000)

## 4. Computing the distribution ##

import math
#[(p^k * q^N-k) * (N_C_k)] formula
def overall_probability(N,k,p,q):
    combination = math.factorial(N) / (math.factorial(k) * math.factorial(N-k))
    probability = p**k * (q**(N-k))
    return(combination * probability)
# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))
p = .39
q = 1-.39
outcome_probs = [overall_probability(max(outcome_counts),i,p,q) for i in outcome_counts]

## 6. Simplifying the computation ##

import scipy
from scipy import linspace
from scipy.stats import binom

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)

p = 0.39
N = 30
dist = binom.pmf(outcome_counts,N,p)
plt.bar(outcome_counts,dist)
plt.show()

## 8. Computing the mean of a probability distribution ##

dist_mean = None
dist_mean = 30* .39

## 9. Computing the standard deviation ##

dist_stdev = None
N = 30
p = .39
dist_stdev = (N * p* (1-p))**(1/2)

## 10. A different plot ##

from scipy import linspace
from scipy.stats import binom


outcome_counts = linspace(0,10,11)
dist_10 = binom.pmf(outcome_counts,10,.39)
plt.xlim(0.0 , 12.0)
plt.bar(outcome_counts,dist_10)
plt.show()


outcome_counts = linspace(0,100,101)
dist_100 = binom.pmf(outcome_counts,100,.39)
plt.xlim(0.0 , 120.0)
plt.bar(outcome_counts,dist_100)
plt.show()

## 12. Cumulative density function ##

from scipy import linspace
from scipy.stats import binom

outcome_counts = linspace(0,30,31)
dist = binom.cdf(outcome_counts, 30, 0.39)
plt.plot(outcome_counts,dist)
plt.show()

## 14. Faster way to calculate likelihood ##

#We will use the cdf to determine how likely or unlikely a probability is. Though keep in mind that
#the cdf distribution isn't exactly normal, but will give us the actual amount of probability in
#a distribution to the left of a given k
from scipy.stats import binom
left_16 =  binom.cdf(16, 30, .39)
right_16 = 1 - binom.cdf(16, 30, .39)