tickets = input('Введите количество билетов: ')
total_price = 0
for ticket in range(int(tickets)):
    age = int(input('Введите возраст посетителя: '))
    if age >= 25:
        total_price += 1390
    elif 18 <= age < 25:
        total_price += 990
    elif 0 < age < 18:
        total_price +=0

if int(tickets) > 3:
    print(total_price*0.9)
else:
    print(total_price)
