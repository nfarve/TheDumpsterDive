import os
from decimal import *

def populate():
    laverde_dumpster = add_dumpster(lat=float_to_decimal(42.35929),
        lng=float_to_decimal(-71.09476),
        des='LaVerdes dumpster behind the MIT Student Center')

    produce = add_foodgroup(name='Produce')
    meat = add_foodgroup(name='Meat')
    dairy = add_foodgroup(name='Dairy')

def add_dumpster(lat, lng, des):
    d = Dumpster.objects.get_or_create(latitude=lat, longitude=lng, 
        description=des)
    return d

def add_foodgroup(name):
    fg = FoodGroup.objects.get_or_create(name=name)
    return fg

def add_food(name,dr,fg):
    f = Food.objects.get_or_create(name=name, dumpster=d, foodgroup=fg)
    return f

def float_to_decimal(f):
    "Convert a floating point number to a Decimal with no loss of information"
    n, d = f.as_integer_ratio()
    numerator, denominator = Decimal(n), Decimal(d)
    ctx = Context(prec=60)
    result = ctx.divide(numerator, denominator)
    while ctx.flags[Inexact]:
        ctx.flags[Inexact] = False
        ctx.prec *= 2
        result = ctx.divide(numerator, denominator)
    return result

# Start execution here!
if __name__ == '__main__':
    print "Starting TheDumpsterDive population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TheDumpsterDive.settings')
    from TheDive.models import Dumpster, FoodGroup, Food
    populate()
