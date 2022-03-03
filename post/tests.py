from django.test import TestCase
from django.urls import reverse
from .models import Post
#  here , database is uded , so, TestCase is used
class PostTests(TestCase):

	def setUp(self):
		Post.objects.create(text="Post created for test")

	def test_text_content(self):
		post=Post.objects.get(id=1)
		expected_object_name=f'{post.text}'
		self.assertEquals(expected_object_name,'Post created for test')

	def test_post_list_view(self):
		response=self.client.get(reverse('posts'))
		self.assertEquals(response.status_code,200)
		self.assertContains(response,'Post created for test')
		self.assertTemplateUsed(response,'posts.html')