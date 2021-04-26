from django.test import TestCase
from django.urls.base import reverse_lazy

index_path = reverse_lazy('index')


class Test(TestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_index_template_has_sharedData(self):
        r = self.client.get(index_path)
        self.assertContains(r, 'sharedData')

    def test_index_context_has_sharedData(self):
        r = self.client.get(index_path)
        self.assertIn('sharedData', r.context.keys())

    def test_index_has_react_root(self):
        r = self.client.get(index_path)
        self.assertContains(r, '<div id="root"></div>')
