# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

#1. The language spoken the most in Switzerland is the same as in Spain.
most_language_spoken_in_switzerland = "Swiss German)"
most_language_spoken_in_spain = 'Castilian Spanish'
print(most_language_spoken_in_switzerland!= most_language_spoken_in_spain)

#2. The most prevalent religion in Switzerland is the same as in Spain.
most_prevalent_religion_in_switzerland = "Roman Catholic"
most_prevalent_religion_in_spain = "Roman Catholic"
print(most_prevalent_religion_in_switzerland == most_prevalent_religion_in_spain)

#3. The name length of Spain's capital does not equal that of Switzerland.

length_of_spain_capital = "Madrid"
print(len(length_of_spain_capital))

length_of_switzerland_capital = "Bern"
print(len(length_of_switzerland_capital))

print(length_of_spain_capital!=length_of_switzerland_capital)

#4. Switzerland's GDP is greater than Spain's GDP.
spain_GDP_per_capita = 20,900
switzerland_GDP_per_capita = 67,885
print( switzerland_GDP_per_capita > spain_GDP_per_capita)

#5. The population growth is less than 1% in Switzerland and Spain.
spain_population_growth = 0.67
switzerland_population_growth = 0.66
print(spain_population_growth < 1, switzerland_population_growth < 1)

#6. At least one of the two countries has a population count of over 10 million.

spain_population_in_million = 50
switzerland_population_in_million = 8.4
print(spain_population_in_million > 10, switzerland_population_in_million > 10)

#7. Exactly one of the two countries has a population count of over 10 million.

print(spain_population_in_million)