per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Сумма: '))

deposit_with_banks = []
deposit = []
for key,value in per_cent.items():
    deposit_with_banks.append(f'{key} : {int((money*0.01)*value)}')
    deposit.append(int((money*0.01)*value))

print('В этих банках можно зарабоать за год:', ", ".join(deposit_with_banks))

print(f'Максимальную прибыль можно получить - {max(deposit, key=int)}')
