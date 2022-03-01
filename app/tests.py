from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Image, Location, Category


# Create your tests here.
class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        """Creating a new location and saving it"""
        self.place = Location(location_name='Nairobi')
        self.place.save_location()


    def test_instance(self):
        """Testing instance"""
        self.assertTrue(isinstance(self.place, Location))


    def test_save_method(self):
        """Testing Save Method"""
        self.place.save_location()
        places = Location.objects.all()
        self.assertTrue(len(places) > 0)


    def test_update_method(self):
        """Testing Update Method"""
        self.place.update_location(name="Nyeri")
        places = Location.objects.all()
        self.assertTrue(len(places) > 0)


