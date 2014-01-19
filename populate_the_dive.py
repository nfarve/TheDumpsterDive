import os
from decimal import *

def populate():
    laverde_dumpster = add_dumpster(lat=float_to_decimal(42.35929),
        lng=float_to_decimal(-71.09476),
        des='LaVerdes dumpster behind the MIT Student Center')

    wholefood_dumpster = add_dumpster(lat=float_to_decimal(42.36186),
        lng=float_to_decimal(-71.11427),
        des='Whole Foods dumpster')

    traderjoe_dumpster = add_dumpster(lat=float_to_decimal(42.35807),
        lng=float_to_decimal(-71.11425),
        des='Trader Joe dumpster')

    produce = add_foodgroup(name='Produce')
    meat = add_foodgroup(name='Meat')
    dairy = add_foodgroup(name='Dairy')

    food1 = add_food(name='Broccoli', d=laverde_dumpster, 
        fg=produce)
    food2 = add_food('Kobe beef', laverde_dumpster, meat)
    food3 = add_food('Goat cheese', laverde_dumpster, dairy)

    food4 = add_food('Asparagus', wholefood_dumpster, produce)
    food5 = add_food('Pork tenderloin', wholefood_dumpster, meat)
    food6 = add_food('Almond milk', wholefood_dumpster, dairy)

    food7 = add_food('Pomegranate', traderjoe_dumpster, produce)
    food8 = add_food('Venizon', traderjoe_dumpster, meat)
    food9 = add_food('Gouda cheese', traderjoe_dumpster, dairy)


def add_dumpster(lat, lng, des):
    d = Dumpster.objects.get_or_create(latitude=lat, longitude=lng, 
        description=des)[0]
    return d

def add_foodgroup(name):
    fg = FoodGroup.objects.get_or_create(name=name)[0]
    return fg

def add_food(name,d,fg):
    f = Food.objects.get_or_create(name=name, dumpster=d, foodgroup=fg)[0]
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
