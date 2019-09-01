from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils.html import escape

from accounts.models import User
from board.models import Post, Comment


class PostTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User()
        user.username = '유저명'
        user.password = 'abcd'
        user.email = 'abc@abc.com'
        user.first_name = '유'
        user.last_name = '저명'
        user.save()

    def test_post_save(self):
        post = Post()
        post.user = User.objects.get(pk=1)
        post.title = '제목'
        post.content = '내용'
        post.tags = 'abc'
        post.status = 'd'
        post.save()

        saved_post = Post.objects.first()
        self.assertEqual(saved_post, post)



