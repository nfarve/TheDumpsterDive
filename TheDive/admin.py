from django.contrib import admin

# Register your models here.from TheDive.models import Category, Page


from TheDive.models import Dumpster, FoodGroup, Food

# Register your models here.
admin.site.register(Dumpster)
admin.site.register(FoodGroup)
admin.site.register(Food)


