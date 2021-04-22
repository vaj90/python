rates = {
    'mortgage': {
        'home': 5.5,
        'auto': 3.5
    },
    'loan': {
        'secured': 7.5,
        'unsecured': 8.5
    }
}

print(rates['mortgage']['home'])
print(rates['loan']['unsecured'])
rates['mortgage']['auto'] = 6.3
rates['mortgage']['secured'] = 9.6
print("\n")
for i in rates:
    for j in rates[i]:
        print(i, ":", j, "=", rates[i][j])
print("\n")

towatch = {
    'educational': {
        'youth': {
            'Youth Show 1': 'Showtime for this show1',
            'Youth Show 2': 'Showtime for this show2',
        },
        'kids': {
            'Barney': '4pm weekdays',
            'Magic school bus': '8am daily'
        }
    },
    'comedy': {
        'teenage': {
            'Teenage show 1': 'Friday at 6 PM',
            'Teenage show 2': 'Saturdays'
        },
        '18plus': {
            'Scary movie': '11pm Friday',
            'Documentaries': '11am Saturday'
        }
    }
}

print(towatch['educational']['kids']['Barney'])
towatch['educational']['youth']['Youth Show 1'] = 'no entry'

for i in towatch:
    for j in towatch[i]:
        for k in towatch[i][j]:
            print(i, ":", j, ":", k, "=", towatch[i][j][k])