weight = float(input("Please enter your weight: "))
unit = str(input("Please enter 1 for lbs, and 2 for kg: "))

if unit == '1':
    weightkg = round((weight * 0.453592), 2)
    print(f'Your weight in kg is {weightkg}')
else:
    weightlbs = round((weight * 2.20462), 2)
    print(f'Your weight in lbs is {weightlbs}')