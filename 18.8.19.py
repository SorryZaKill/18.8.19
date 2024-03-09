price =  0
ticket = (int(input("Введите количество билетов:")))
for age in range(ticket):
    age = (int(input("Введите возраст:")))
    if age <18:
        price += 0
    elif age >= 18 and age <=25:
        price += 990
    elif age > 25:
        price += 1390
if ticket >3:
    price -= price / 100 * 10
print("Стоимость билетов", price)
