## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt

print("Group A:", weight_lost_a)
print("Group B:", weight_lost_b)

mean_group_a = np.mean(weight_lost_a)
print(mean_group_a)

mean_group_b = np.mean(weight_lost_b)
print(mean_group_b)

plt.hist(weight_lost_a)
plt.show()
plt.hist(weight_lost_b)
plt.show()

## 4. Test statistic ##

mean_difference = mean_group_b- mean_group_a
print(mean_difference)

## 5. Permutation test ##

import numpy as np
print(all_values)
mean_differences = []
for i in range(0,1000):
    group_a = []
    group_b = []
    for val in all_values:
        a = np.random.rand()
        if a >= 0.5:
            group_a.append(val)
        else:
            group_b.append(val)
    group_a_mean = np.mean(group_a)
    group_b_mean = np.mean(group_b)
    iteration_mean_difference = group_b_mean - group_a_mean
    mean_differences.append(iteration_mean_difference)
plt.hist(mean_differences)

## 7. Dictionary representation of a distribution ##

sampling_distribution = {}

for diff in mean_differences:
    if sampling_distribution.get(diff,False):
        sampling_distribution[diff] +=1
    else:
        sampling_distribution[diff] = 1

## 8. P value ##

frequencies = []
for key in sampling_distribution:
   
    if key >= 2.52:
        frequencies.append(key)
total_freq = np.sum(frequencies)
p_value = total_freq / 1000
print(p_value)