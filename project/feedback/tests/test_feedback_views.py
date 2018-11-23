from django.test import TestCase, Client

class BaseTest(TestCase):

    def setUp(self):
        self.client = Client()


class FeedbackViewTest(BaseTest):

    def test_uses_right_template(self):
        response = self.client.get('/feedback/')
        self.assertTemplateUsed(response, 'feedback/feedback.html')
