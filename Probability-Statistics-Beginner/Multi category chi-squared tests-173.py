## 2. Calculating expected values ##

males_over50k = .669 * .241 * 32561
males_under50k = .669 * .759 * 32561
females_over50k = .331 * .241 * 32561
females_under50k = .331 * .759 * 32561

## 3. Calculating chi-squared ##

expected_values = [5249.8, 2597.4,16533.5, 8180.3]
observed_values = [6662, 1179, 15128, 9592]
sq_values = []
chisq_gender_income = 0
for i, obs in enumerate(observed_values):
    expect = expected_values[i]
    sq_values.append( (obs - expect)**2/expect )
chisq_gender_income = sum(sq_values)

## 4. Finding statistical significance ##

from scipy.stats import chisquare
import numpy as np

expected_values = [5249.8, 2597.4, 16533.5, 8180.3]
observed_values = [6662, 1179, 15128, 9592]
chisq_value , pvalue_gender_income = chisquare(observed_values, expected_values)
print(pvalue_gender_income)

## 5. Cross tables ##

import pandas as pd
table = pd.crosstab(income["sex"], income["race"])
print(table)

## 6. Finding expected values ##

import pandas as pd
from scipy.stats import chi2_contingency

#Obtain the crosstab observed values between sex and race
observed = pd.crosstab(income["sex"], income["race"])
print(observed)
#Obtain the chi-square value, p value, degrees of freedom, and the expected value
chisq_value, pvalue_gender_race, df , expected = chi2_contingency(observed)
print(chisq_value)
print(pvalue_gender_race)
print(df)
print(expected)

