from django.test import TestCase, Client
from feedback.models import Feedback

class BaseTest(TestCase):

    def setUp(self):
        Feedback.objects.create(title='title1')
        Feedback.objects.create(title='title2')

        self.client = Client()


class FeedbackViewTest(BaseTest):

    def test_uses_right_template(self):
        response = self.client.get('/feedback/')
        self.assertTemplateUsed(response, 'feedback/feedback.html')

    def test_passes_right_items(self):
        response = self.client.get('/feedback/')
        items = Feedback.objects.all()
        for response_item in response.context['items']:
            self.assertIn(response_item.title, [item.title for item in items])
            
