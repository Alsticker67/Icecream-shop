from django.contrib.auth.models import User
from django.test import TestCase

from home.catalog import CATEGORIES
from home.models import Contact


class PageTests(TestCase):
    def test_public_pages_load(self):
        for url in ["/", "/about", "/services", "/contact", "/login", "/familypack"]:
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 200)

    def test_every_category_page_loads(self):
        for category in CATEGORIES:
            with self.subTest(category=category["slug"]):
                response = self.client.get(f"/services/{category['slug']}")
                self.assertContains(response, category["products"][0]["name"])

    def test_unknown_category_is_404(self):
        response = self.client.get("/services/does-not-exist")
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "This scoop melted", status_code=404)

    def test_familypack_is_public_and_lists_packs(self):
        response = self.client.get("/familypack")
        self.assertContains(response, "Choco-Vanilla Combo")
        self.assertContains(response, "&#8377;429")

    def test_prices_in_rupees_with_from_label(self):
        response = self.client.get("/services/parties-events")
        self.assertContains(response, "&#8377;7,999")
        self.assertContains(response, "From")

    def test_search_covers_all_categories(self):
        response = self.client.get("/services", {"q": "chocolate"})
        self.assertContains(response, "Rich Chocolate")        # family pack
        self.assertContains(response, "Choco-Dip Twin Cones")  # cone
        self.assertNotContains(response, "Tutti Frutti")

    def test_search_with_no_match(self):
        response = self.client.get("/services", {"q": "pizza"})
        self.assertContains(response, "No ice creams match")

    def test_contact_form_saves_and_redirects(self):
        response = self.client.post("/contact", {
            "name": "Test", "email": "t@example.com", "phone": "123", "desc": "Hi",
        })
        self.assertRedirects(response, "/contact")
        self.assertEqual(Contact.objects.count(), 1)


class LoginTests(TestCase):
    def setUp(self):
        User.objects.create_user("tester", password="secret123")

    def test_login_logout_flow(self):
        response = self.client.post("/login", {"username": "tester", "password": "secret123"})
        self.assertRedirects(response, "/")
        self.assertRedirects(self.client.get("/login"), "/")
        self.assertRedirects(self.client.get("/logout"), "/")

    def test_wrong_password_shows_error(self):
        response = self.client.post("/login", {"username": "tester", "password": "wrong"})
        self.assertContains(response, "Invalid username or password")
