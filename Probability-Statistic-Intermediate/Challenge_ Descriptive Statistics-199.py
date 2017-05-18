## 1. Introduction ##

import matplotlib.pyplot as plt
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")

fig = plt.figure(figsize = (5,12))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.set_xlim(0,5.0)
ax2.set_xlim(0,5.0)
ax3.set_xlim(0,5.0)
ax4.set_xlim(0,5.0)

movie_reviews["RT_user_norm"].hist(ax = ax1)
movie_reviews["Metacritic_user_nom"].hist(ax = ax2)
movie_reviews["Fandango_Ratingvalue"].hist(ax = ax3)
movie_reviews["IMDB_norm"].hist(ax = ax4)

## 2. Mean ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return(mean)

column_names = ["RT_user_norm", "Metacritic_user_nom","Fandango_Ratingvalue","IMDB_norm"]

user_reviews = movie_reviews[column_names]
user_review_means = user_reviews.apply(calc_mean)

rt_mean = user_review_means["RT_user_norm"]
mc_mean =user_review_means["Metacritic_user_nom"]
fg_mean =user_review_means["Fandango_Ratingvalue"]
id_mean =user_review_means["IMDB_norm"]
print("RT mean:",rt_mean,"\n","MC_mean:",mc_mean,"\n","FG_mean:",fg_mean,"\n","ID_mean",id_mean)

## 3. Variance and standard deviation ##

def calc_variance(series):
    vals = series.values
    mean = calc_mean(series)
    variance_nonsum = (series-mean)**2
    sum_variance = calc_mean(variance_nonsum)
    return(sum_variance)

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

column_names = ["RT_user_norm", "Metacritic_user_nom","Fandango_Ratingvalue","IMDB_norm"]


user_reviews = movie_reviews[column_names]
user_review_means = user_reviews.apply(calc_mean)

rt_mean = user_review_means["RT_user_norm"]
mc_mean =user_review_means["Metacritic_user_nom"]
fg_mean =user_review_means["Fandango_Ratingvalue"]
id_mean =user_review_means["IMDB_norm"]

user_review_variances = user_reviews.apply(calc_variance)
rt_var = user_review_variances["RT_user_norm"]
mc_var =user_review_variances["Metacritic_user_nom"]
fg_var =user_review_variances["Fandango_Ratingvalue"]
id_var =user_review_variances["IMDB_norm"]

rt_stdev = user_review_variances["RT_user_norm"] **(1/2)
mc_stdev =user_review_variances["Metacritic_user_nom"]**(1/2)
fg_stdev =user_review_variances["Fandango_Ratingvalue"]**(1/2)
id_stdev =user_review_variances["IMDB_norm"]**(1/2)

print("RT Variance:",rt_var)
print("MC Variance:",mc_var)
print("FG Variance:",fg_var)
print("ID Variance:",id_var)
print("RT Standard Deviation:",rt_stdev)
print("MG Standard Deviation:",mc_stdev)
print("FG Standard Deviation:",fg_stdev)
print("ID Standard Deviation:",id_stdev)

## 4. Scatter plots ##

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(4,8))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.set_xlim(0,5.0) 
ax2.set_xlim(0,5.0)
ax3.set_xlim(0,5.0)


ax1.scatter(y=movie_reviews["Fandango_Ratingvalue"],x=movie_reviews["RT_user_norm"])
ax2.scatter(y=movie_reviews["Fandango_Ratingvalue"],x=movie_reviews["Metacritic_user_nom"])
ax3.scatter(y=movie_reviews["Fandango_Ratingvalue"],x=movie_reviews["IMDB_norm"])


## 5. Covariance ##

def calc_covariance(series1, series2):
    vals1 = series1.values
    vals2 = series2.values
    
    vals1_mean = calc_mean(series1)
    vals2_mean = calc_mean(series2)
    
    vals1_diffs =[i-vals1_mean for i in vals1]
    vals2_diffs = [i - vals2_mean for i in vals2]
    
    codeviates = [vals1_diffs[i] * vals2_diffs[i] for i in range(len(vals1))]
    
    covariance = sum(codeviates)/len(codeviates)
    return(covariance)
def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean
rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

print("Covariance between Rotten Tomatoes and Fandango:", rt_fg_covar)
print("Covariance between Metacritic and Fandango", mc_fg_covar)
print("Covariance between IMDB and Fandango", id_fg_covar)

## 6. Correlation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations

def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])
def calc_correlation(series_one, series_two):
    numerator = calc_covariance(series_one, series_two)
    series_one_std = calc_variance(series_one) ** (1/2)
    series_two_std = calc_variance(series_two) ** (1/2)
    denominator = series_one_std * series_two_std
    correlation = numerator / denominator
    return correlation

rt_fg_corr = calc_correlation(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_corr = calc_correlation(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_corr = calc_correlation(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

print("Correlation between Rotten Tomatoes and Fandango", rt_fg_corr)
print("Correlation between Metacritic and Fandango", mc_fg_corr)
print("Correlation between IMDB and Fandango", id_fg_corr)