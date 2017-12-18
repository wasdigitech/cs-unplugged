from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse
from http import HTTPStatus


class ComputationalThinkingURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_computational_thinking_url(self):
        url = reverse("general:computational_thinking")
        self.assertEqual(url, "/en/computational-thinking/")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
