from django.db import models

# Create your models here.
class Location(models.Model):
    name=models.CharField(max_length=60)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self,name):
        self.name=name
        self.save()

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=60)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self,name):
        self.name=name
        self.save()

    def __str__(self):
        return self.name



