from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class BinaryCardsResourceURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.RESOURCE_SLUG = "binary-cards"
        self.RESOURCE_URL_KWARGS = {"resource_slug": self.RESOURCE_SLUG}

    def test_valid_binary_cards_resource_url(self):
        url = reverse("resources:resource", kwargs=self.RESOURCE_URL_KWARGS)
        self.assertEqual(url, "/en/resources/binary-cards/")
