from django.test import TestCase
from archiv.models import HapaPlaceName


class HapaPlaceNameTest(TestCase):
    def setUp(self):
        self.tirana = HapaPlaceName.objects.create(name="Tirana")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        item = HapaPlaceName.objects.get(name="Tirana")
        self.assertEqual(item.name, 'Tirana')
