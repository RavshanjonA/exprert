from django.test import TestCase
from django.urls import reverse

from news.models import Post


class PostModelTestCase(TestCase):
    def setUp(self) -> None:
        Post.objects.create(title="Mavzu",text="yangilik matni")

    def test_context(self):
        post = Post.objects.get(id=1)
        excepted_title = post.title
        excepted_text = post.text
        self.assertEqual(excepted_title,"Mavzu")
        self.assertEqual(excepted_text, "yangilik matni")

class HomePageViewTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(title="Mavzu 2",text="boshqa yangilik")

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'home.html')

