import pandas as pd

# Загрузка данных из CSV-файла
data = pd.read_csv('data.csv')

# Вычисление средней зарплаты всех сотрудников
average_salary = data['salary'].mean()
print(f'Средняя зарплата всех сотрудников: {average_salary:.2f}')

# Отбор сотрудников старше 30 лет
employees_over_30 = data.query("age > 40")

# Вывод списка таких сотрудников
if not employees_over_30.empty:
    print("\nСотрудники старше 30 лет:")
    for index, row in employees_over_30.iterrows():
        print(f"{row['name']}, возраст: {row['age']}, зарплата: {row['salary']}")
else:
    print("\nНет сотрудников старше 30 лет.")