from django.test import TestCase
from taxi.models import Driver, Car, Manufacturer


class DriverModelTest(TestCase):
    def test_str_method(self):
        driver = Driver(username="luke", first_name="Luke",
                        last_name="Skywalker")
        self.assertEqual(str(driver), "luke (Luke Skywalker)")


class CarModelTest(TestCase):
    def test_str_method(self):
        manufacturer = Manufacturer(name="Toyota")
        car = Car(manufacturer=manufacturer, model="Corolla")
        self.assertEqual(str(car), "Corolla")


class ManufacturerModelTest(TestCase):
    def test_str_method(self):
        manufacturer = Manufacturer(name="Ford", country="USA")
        self.assertEqual(str(manufacturer), "Ford USA")
