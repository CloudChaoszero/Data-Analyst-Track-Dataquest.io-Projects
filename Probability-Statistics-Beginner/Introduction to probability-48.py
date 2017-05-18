## 1. Probability basics ##

# Print the first two rows of the data.
print(flags[:2])
most_bars = flags["bars"].idxmax
most_bars_country = flags["name"][most_bars]
print(most_bars_country)

highest_population = flags["population"].idxmax
highest_population_country = flags["name"][highest_population]
print(highest_population_country)

## 2. Calculating probability ##

total_countries = flags.shape[0]
orange_probability = flags[flags["orange"] == 1].shape[0] / total_countries

stripe_probability = flags[flags["stripes"] > 1].shape[0] / total_countries

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5
ten_heads = .5 **10
hundred_heads = .5 **100

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.
red_countries_count = flags[flags["red"]==1].shape[0]
total_countries = flags.shape[0]
three_red = (red_countries_count/total_countries) * (red_countries_count-1)/(total_countries-1) * (red_countries_count-2)/(total_countries-2) 

## 5. Disjunctive probability ##

start = 1
end = 18000
def count_evenly_divisible(start, end, div):
    divisible_count = 0
    for i in range(start,end+1):
        if (i % div) == 0:
            divisible_count +=1
    return(divisible_count)

hundred_prob = count_evenly_divisible(start, end, 100) / end
seventy_prob = count_evenly_divisible(start, end, 70) / end

## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None
length = flags.shape[0]
#Finding the probability of a flag having red or orange as a color.
red = flags[flags["red"]==1].shape[0]
orange = flags[flags["orange"]==1].shape[0]
red_and_orange = flags[(flags["red"]==1) & (flags["orange"]==1)].shape[0]
red_or_orange = (red/length) + (orange/length)-(red_and_orange)/length



#Finding the probability of a flag having at least one stripes or at least one bars
stripes = flags[flags["stripes"]>=1].shape[0]
bars = flags[flags["bars"]>=1].shape[0]
stripes_and_bars = flags[(flags["stripes"]>=1) & (flags["bars"]>=1)].shape[0]
stripes_or_bars = (stripes/length) + (bars/length)-(stripes_and_bars)/length


## 7. Disjunctive probabilities with multiple conditions ##

heads_or = None
all_three_tails = (1/2 * 1/2 * 1/2)
heads_or = 1 - all_three_tails