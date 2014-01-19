from django.db import models

class Dumpster(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.description

class FoodGroup(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=128)
    dumpster = models.ForeignKey(Dumpster)
    foodgroup = models.ForeignKey(FoodGroup)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.name
