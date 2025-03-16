print("To calculate Your Age ")
y = int(input('Year as : yyyy :'))
m = int(input('Moth as : mm : '))
d = int(input('Date as : dd : '))


def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)
ageCalculator(y, m, d)