import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class FeedbackTestBase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
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
        time.sleep(5)