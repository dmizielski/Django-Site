from django.test import TestCase
from django.utils import timezone
from .models import Post


# Create your tests here.
class PostsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.object.create(title='Post101', content='abcd',
                           date_posted=timezone.now, author='damian')

    def test_posts(self):
        """ Check if Post data are valid """
        newPost = Post.object.get(title='Post101')
        self.assertEqual(newPost.title, 'Post101')
