from django.test import SimpleTestCase
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_blog_page_status_code(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code,200)

    def test_help_page_status_code(self):
        response = self.client.get('/help/')
        self.assertEqual(response.status_code, 200)