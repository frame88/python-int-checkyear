
year = int(input('Inserisci un anno: '))

if year%4 == 0 and year%100 != 0 or year%400 == 0:
    print('anno bisestile')
else:
    print('anno non bisestile')

