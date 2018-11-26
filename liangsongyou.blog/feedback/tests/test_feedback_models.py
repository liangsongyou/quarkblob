from django.test import TestCase

from feedback.models import Feedback

class FeedbackModelTest(TestCase):

    def setUp(self):
        item = Feedback.objects.create(title='Test title')

        self.item = item

    def test_saving_items(self):
        self.assertEqual(self.item.title,'Test title')

    def test_str(self):
        self.assertEqual('Test title', self.item.__str__())

    def test_absolute_url(self):
        self.assertEqual('/feedback/test-title/',self.item.get_absolute_url())