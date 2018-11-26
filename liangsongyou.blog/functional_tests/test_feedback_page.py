import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

from feedback.models import Feedback

class FeedbackTestBase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        Feedback.objects.create(title='Best blog ever!')
        Feedback.objects.create(title='Django rules!')
        super().setUpClass()
        cls.browser = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()


class FeedbackPageTests(FeedbackTestBase):

    def test_feedback_page(self):

        self.browser.get('%s%s' % (self.live_server_url, '/feedback/'))
        self.assertIn('Feedback',self.browser.title)
        

        h1 = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('Feedback',h1)

        feedback_items = self.browser.find_element_by_class_name('feedback-items').text
        self.assertIn('Best blog ever!', feedback_items)
        self.assertIn('Django rules!', feedback_items)

        input = self.browser.find_element_by_id('id_title')
        time.sleep(2)
        input.send_keys('Awesome blog!')
        input.send_keys(Keys.ENTER)
        time.sleep(5)
        feedback_items = self.browser.find_element_by_class_name('feedback-items').text
        self.assertIn('Awesome blog!',feedback_items)



























