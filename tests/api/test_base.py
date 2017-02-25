import requests
import testtools

from app import routs


class Base(testtools.TestCase):
    def setUp(self):
        super(Base, self).setUp()
        url = 'http://localhost:5000'
        self.url = url

    def test_on_event_page_not_found(self):
        not_found = routs.page_not_found()
        self.assertEqual(302, not_found.status_code)

    def test_send_message(self):
        msg = requests.post(url=self.url, data='Hello.')
        self.assertEqual(200, msg.status_code)
