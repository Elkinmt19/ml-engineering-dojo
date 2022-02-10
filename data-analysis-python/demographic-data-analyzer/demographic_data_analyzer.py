#Built-in imports
import sys

# External imports
import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.unique().shape[0]

    # What is the average age of men?
    average_age_men = df.age[df.sex == "Male"].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df.education[df.education == "Bachelors"].count()*100/df.education.count()

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?


    # with and without `Bachelors`, `Masters`, or `Doctorate`
    hi_edu = df.salary[df["education-num"] >= 13]
    lo_edu = df.salary[df["education-num"] < 13]  

    # percentage with salary >50K
    higher_education_rich = hi_edu[hi_edu == ">50K"].count()*100/hi_edu.count()
    lower_education_rich = lo_edu[lo_edu == ">50K"].count()*100/lo_edu.count()

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    peo_h_min = df.salary[df["hours-per-week"] == min_work_hours]

    rich_percentage = peo_h_min[peo_h_min == "<50K"].count()*100/peo_h_min.count()

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


def main():
    calculate_demographic_data()

if __name__ == "__main__":
    sys.exit(main())