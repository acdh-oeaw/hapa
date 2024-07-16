from django.contrib.auth.models import User
from django.test import Client, TestCase

from django.urls import reverse


class WebpageTest(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user("temporary", "temp@gmail.com", "temporary")

    def test_001_webpage(self):
        rv = self.client.get("/")
        self.assertEqual(rv.status_code, 302)
        rv = self.client.get("/accounts/login/")
        self.assertContains(rv, "Username")
        form_data = {"username": "temporary", "password": "temporary"}
        rv = self.client.post("/accounts/login/", form_data, follow=True)
        self.assertContains(rv, "Belege")
        rv = self.client.get("/logout/", follow=True)
        self.assertContains(rv, "You've signed out")
        form_data = {"username": "non_exist", "password": "temporary"}
        rv = self.client.post("/accounts/login/", form_data, follow=True)
        self.assertContains(rv, "user does not exist")

    def test_002_imprint(self):
        url = reverse("webpage:imprint")
        rv = self.client.get(url)
        self.assertContains(rv, "Legal disclosure")
