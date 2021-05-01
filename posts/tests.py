from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostModelTest(TestCase):
    """
    Test case for database.
    Create a test database, that we can check against.
    """

    def setUp(self):
        """
        To create a new database that has just 1 entry.
        """
        Post.objects.create(text='testing my text.')

    def test_text_content(self):
        """
        assert = state a fact confidentially. "declare / state / दाबी गर्नु"
        assertEqual() -> Fail if the two objects are unequal as determined by the '==' operator.
        """
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'testing my text.')


class HomepageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='another text.')

    def test_view_url_exists_at_proper_location(self):
        """
        To test if view url exists.
        """
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp=self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp=self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
