#Method two of how to solve the life in a year challenge
age = int(input("What is your current age?: "))

ninety_years_in_days = 90 * 365

ninety_years_in_weeks = 90 * 52

ninety_years_in_months = 90 * 12

user_age_in_days = ninety_years_in_days - (age * 365)

user_age_in_weeks = ninety_years_in_weeks - (age * 52)

user_age_in_months = ninety_years_in_months - (age * 12)

print(f"You have {user_age_in_days} days, {user_age_in_weeks} weeks, and {user_age_in_months} months left till you turn 90 years.")