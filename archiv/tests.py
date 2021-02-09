from django.test import TestCase
from gn_places.utils import gn_get_or_create

from archiv.models import HapaPlaceName

LINZ_GN = "https://www.geonames.org/2772400/linz.html"


class HapaPlaceNameTest(TestCase):
    def setUp(self):
        self.linz = HapaPlaceName.objects.create(name="Linz")
        self.linz_gn = gn_get_or_create(LINZ_GN)

    def test_001_create_object(self):
        """Simple test to check if object was created"""
        item = HapaPlaceName.objects.get(name="Linz")
        self.assertEqual(item.name, 'Linz')

    def test_002_check_coords_fetch_from_rel_gn_entry(self):
        item = HapaPlaceName.objects.get(name="Linz")
        item.geonames = self.linz_gn
        item.save()
        self.assertEqual(item.lat, self.linz_gn.gn_lat)

    def test_003_historic_place(self):
        item = self.linz
        self.assertEqual(item.historic, False)

    def test_004_new_text_fields(self):
        item = self.linz
        item.wortbildung = "lorem ipsum"
        item.etymology = "lorem ipsum"
        item.syntax = "lorem ipsum"
        item.save()
        item = HapaPlaceName.objects.get(wortbildung="lorem ipsum")
        self.assertEqual(item.wortbildung, "lorem ipsum")
        item = HapaPlaceName.objects.get(etymology="lorem ipsum")
        self.assertEqual(item.etymology, "lorem ipsum")
        item = HapaPlaceName.objects.get(syntax="lorem ipsum")
        self.assertEqual(item.syntax, "lorem ipsum")
