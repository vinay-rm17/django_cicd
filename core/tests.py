from rest_framework.test import APITestCase
from .models import Item

class ItemAPITests(APITestCase):
    def test_create_item(self):
        url = "/api/items/"
        data = {"name": "Pen", "quantity": 10}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Item.objects.count(), 1)

        item = Item.objects.first()
        self.assertEqual(item.name, "Pen")
        self.assertEqual(item.quantity, 10)

    def test_get_items(self):
        Item.objects.create(name="Book", quantity=3)

        response = self.client.get("/api/items/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["name"], "Book")
