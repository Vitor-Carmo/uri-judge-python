salary = float(input())

data = '''
+========================================+
| Salário	Percentual      |de Reajuste |
+========================================+
|    0       -  400.00              |15% |
|    400.01  -  800.00              |12% |
|    800.01  -  1200.00             |10% |
|    1200.01 -  2000.00             | 7% |
|    Acima de   2000.00             | 4% |
+========================================+
'''

if salary <= 400:
    percentage = 0.15
    readjustment = salary * percentage
    new_salary = salary  + readjustment

elif salary <= 800:
    percentage = 0.12
    readjustment = salary * percentage
    new_salary = salary  + readjustment

elif salary <= 1200:
    percentage = 0.10
    readjustment = salary * percentage
    new_salary = salary  + readjustment

elif salary <= 2000:
    percentage = 0.07
    readjustment = salary * percentage
    new_salary = salary  + readjustment

else:
    percentage = 0.04
    readjustment = salary * percentage
    new_salary = salary  + readjustment

print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %'.format(new_salary, readjustment, (int(percentage * 100))))