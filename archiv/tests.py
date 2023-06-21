from django.apps import apps

from django.test import TestCase, Client
from django.contrib.auth.models import User

from gn_places.utils import gn_get_or_create

from archiv.models import HapaPlaceName

LINZ_GN = "https://www.geonames.org/2772400/linz.html"
MODELS = list(apps.all_models["archiv"].values())
client = Client()
USER = {"username": "testuser", "password": "somepassword"}


class HapaPlaceNameTest(TestCase):
    def setUp(self):
        self.linz = HapaPlaceName.objects.create(name="Linz")
        self.linz_gn = gn_get_or_create(LINZ_GN)
        User.objects.create_user(**USER)

    def test_001_create_object(self):
        """Simple test to check if object was created"""
        item = HapaPlaceName.objects.get(name="Linz")
        self.assertEqual(item.name, "Linz")

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

    def test_005_listviews(self):
        for x in MODELS:
            try:
                url = x.get_listview_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_006_detailviews(self):
        for x in MODELS:
            item = x.objects.first()
            try:
                url = item.get_absolute_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {"pk": item.id})
                self.assertEqual(response.status_code, 200)

    def test_007_editviews(self):
        client.login(**USER)
        for x in MODELS:
            item = x.objects.first()
            try:
                url = item.get_edit_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {"pk": item.id})
                self.assertEqual(response.status_code, 200)

    def test_008_createviews_not_logged_in(self):
        for x in MODELS:
            item = x.objects.first()
            try:
                url = item.get_createview_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {"pk": item.id})
                self.assertEqual(response.status_code, 302)

    def test_009_createviews_logged_in(self):
        client.login(**USER)
        for x in MODELS:
            item = x.objects.first()
            try:
                url = item.get_createview_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {"pk": item.id})
                self.assertEqual(response.status_code, 200)
