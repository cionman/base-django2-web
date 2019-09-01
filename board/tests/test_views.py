from django.test import TestCase, Client
from django.urls import resolve
from django.utils.html import escape

from board.forms import PostForm
from board.models import Post
from board.views_cbv import post_list


class BoardViewTest(TestCase):

    def test_post_list_view_resolve(self):
        found = resolve('/board')  # resolve는 URL을 해석해서 일치하는 뷰함수를 찾는다.
        self.assertEqual(found.func, post_list)

    def test_post_list_view(self):
        response = self.client.get('/board')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'board/post_list.html')

    def test_post_new_get_view(self):
        response = self.client.get('/board/new')
        self.assertIsInstance(response.context['form'], PostForm)

    # def test_post_new_post_view(self):
    #     self.client = Client(enforce_csrf_checks=True)
    #     self.client.get("/board/new")
    #     response = self.client.post('/board/new',
    #                                 {'user': "1"
    #                                       , 'title' : '제목1'
    #                                       , 'content': '내용'
    #                                       , 'photo' : ''
    #                                       , 'tags' : ''
    #                                       , 'lnglat' : ''
    #                                       , 'status' : ''
    #                                         , 'csrfmiddlewaretoken': self.client.cookies['csrftoken'].value
    #                                       })
    #     post = Post.objects.first()
    #     self.assertRedirects(response, '/board/%d' % (post.id,))


