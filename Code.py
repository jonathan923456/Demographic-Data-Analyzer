#Demographic Data Analyzer

import pandas as pd
import numpy as np


# Read data from file
df = pd.read_csv("adult.data.csv")
#df.head()

# How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
race_count = df["race"].value_counts().tolist()
#print(race_count)

# What is the average age of men?
average_age_men = df[df["sex"] == "Male"]["age"]
average_age_men = round(np.mean(average_age_men) , 1 )
#print(average_age_men)

# What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = len(df[df["education"] == "Bachelors"])
total_education = len(df["education"])
percentage_bachelors = round(100* (percentage_bachelors/total_education) , 1)
#print(percentage_bachelors)
# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
# What percentage of people without advanced education make more than 50K?

higher_education2 = df.loc[(df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate")][df["salary"] == ">50K"]
higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
higher_education_rich = round(100 * (len(higher_education2)/ len(higher_education)), 1)
#print(higher_education_rich)

lower_education2 = df.loc[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])][df["salary"] == ">50K"]
lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
lower_education_rich = round(100 * (len(lower_education2)/ len(lower_education)), 1)
#print(lower_education_rich)

# What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = df["hours-per-week"].min()
#print(min_work_hours)

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
min_work = df.loc[(df["hours-per-week"] == 1)]
num_min_workers = df.loc[(df["hours-per-week"] == 1) & (df["salary"] == ">50K")]

rich_percentage = round(100 * len(num_min_workers) / len(min_work) , 1)
#print(rich_percentage)

# What country has the highest percentage of people that earn >50K?
new_df = df.loc[(df["salary"] == ">50K")]["native-country"].value_counts()
new_df2 = df["native-country"].value_counts()

richest = (new_df / new_df2).max()
#print(richest)

highest_earning_country = (new_df/new_df2).sort_values(ascending = False).index[0]
highest_earning_country_percentage = round(100 * richest, 1 )
#print(highest_earning_country)
#print(highest_earning_country_percentage)

# Identify the most popular occupation for those who earn >50K in India.
india = df.loc[(df["salary"] == ">50K") & ( df["native-country"] == "India")]["occupation"]
top_IN_occupation = pd.Series.mode(india)[0]
#print(top_IN_occupation)
