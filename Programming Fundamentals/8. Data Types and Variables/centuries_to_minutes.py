centuries_input = int(input())

years = centuries_input * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f'{centuries_input} centuries = {years:.0f} years = {days:.0f} days = {hours:.0f} hours = {minutes:.0f} minutes ')