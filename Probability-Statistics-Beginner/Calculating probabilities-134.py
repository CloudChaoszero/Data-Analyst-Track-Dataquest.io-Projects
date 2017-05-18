## 2. Probability of renting bikes ##

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")

# Find the number of days the bikes rented exceeded the threshold.
days_over_threshold = bikes[bikes["cnt"] > 2000].shape[0]
# Find the total number of days we have data for.
total_days = bikes.shape[0]

# Get the probability that more than 2000 bikes were rented for any given day.
probability_over_2000 = days_over_threshold / total_days
print(probability_over_2000)

bikes_4000 = bikes[bikes["cnt"]>4000].shape[0]
probability_over_4000 = bikes_4000 / total_days
print(probability_over_4000)

## 4. Calculating probabilities ##

# Enter your code here.
# There are three combinations in which we can have one coin heads.
# HTT, THT, TTH
# Each combination's probability is (.5 * .5 * .5)
combination_prob = (.5 * .5 * .5) 
# The probability for one combination is in combination_prob -- multiply by the three possible combinations.
coin_1_prob = 3 * combination_prob

## 6. Calculating the number of combinations ##

sunny_1_combinations = None

sunny_1_combinations = 5

## 8. Finding the number of combinations ##

import math
def find_outcome_combinations(N, k):
    # Calculate the numerator of our formula.
    numerator = math.factorial(N)
    # Calculate the denominator.
    denominator = math.factorial(k) * (math.factorial(N-k))
    # Divide them to get the final value.
    return(numerator/denominator)
combinations_7 = find_outcome_combinations(10, 7)
combinations_8 = find_outcome_combinations(10, 8)
combinations_9 = find_outcome_combinations(10, 9)

## 10. Calculating the probability of one combination ##

import math

prob_combination_3 = .7 *.7 *.7 *.3 *.3

## 12. Function to calculate the probability of a single combination ##

import math
#Probability given
p = .6
#Complement Probability given
q = .4

#Per combination probability that takes in requested days of scenario and their respective probabilities
def prob_combination(p,q,days, total_days):
    probability = p**(days) * q**(total_days-days)
    return(probability)

#Combination count functiojn
def combination_count(days, total_days):
    #nCk formula
    count = math.factorial(total_days) /(math.factorial(days)* math.factorial(total_days-days))
    
    return(count)

prob_8 = prob_combination(p,q,8,10) * combination_count(8,10)
prob_9 = prob_combination(p,q,9,10)* combination_count(9,10)
prob_10 = prob_combination(p,q,10,10)* combination_count(10,10)