from datetime import datetime

DIGITS = {
    "0": ["***", "* *", "* *", "* *", "***"],
    "1": ["  *", "  *", "  *", "  *", "  *"],
    "2": ["***", "  *", "***", "*  ", "***"],
    "3": ["***", "  *", "***", "  *", "***"],
    "4": ["* *", "* *", "***", "  *", "  *"],
    "5": ["***", "*  ", "***", "  *", "***"],
    "6": ["***", "*  ", "***", "* *", "***"],
    "7": ["***", "  *", "  *", "  *", "  *"],
    "8": ["***", "* *", "***", "* *", "***"],
    "9": ["***", "* *", "***", "  *", "***"],
}

def get_day_of_week(day, month, year):
    date = datetime(year, month, day)
    return date.strftime("%A")

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_age(birth_day, birth_month, birth_year):
    today = datetime.now()
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    return age

def print_date_with_stars(day, month, year):
    date_str = f"{day:02}{month:02}{year}"
    ascii_art = [""] * 5  
    for char in date_str:
        if char in DIGITS:  
            for i in range(5):
                ascii_art[i] += DIGITS[char][i] + " "  
    
    print("\n".join(ascii_art))

birth_day = int(input("Введите день рождения: "))
birth_month = int(input("Введите месяц рождения: "))
birth_year = int(input("Введите год рождения: "))

day_of_week = get_day_of_week(birth_day, birth_month, birth_year)
is_leap = "да" if is_leap_year(birth_year) else "нет"
age = calculate_age(birth_day, birth_month, birth_year)

print(f"День недели: {day_of_week}")
print(f"Високосный год: {is_leap}")
print(f"Возраст: {age} лет")
print("Дата рождения в стиле электронного табло:")
print_date_with_stars(birth_day, birth_month, birth_year)
