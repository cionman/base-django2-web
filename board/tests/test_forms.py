from django.test import TestCase
from board.forms import PostForm
from board.models import Post


class PostFormTest(TestCase):

    def test_post_form(self):
        form = PostForm()
        self.assertIn('<select name="user" required id="id_user">', form.as_p())




