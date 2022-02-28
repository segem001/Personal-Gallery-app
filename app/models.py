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



class Image(models.Model):
    name=models.CharField(max_length=60)
    description=models.TextField(max_length=1500)
    image=models.ImageField(upload_to='djangofolder/',blank=True)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self,name,description,image,location,category):
        self.name=name
        self.description=description
        self.image=image
        self.location=location
        self.category=category
        self.save()


    @classmethod
    def get_image_by_id(cls,name_id):
        output=cls.objects.get(id=name_id)
        return output

    @classmethod
    def search_image(cls,category):
        image_output=cls.objects.filter(category__name=category)
        return image_output
    @classmethod
    def filter_by_location(cls,location):
        image_output3 = cls.objects.filter(location__name=location)
        return image_output3




    def __str__(self):
        return self.name
