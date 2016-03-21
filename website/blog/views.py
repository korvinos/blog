from django.shortcuts import render
from django.http import HttpResponse
from models import Post, PostManager

# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request):
    post_list = Post.objects.order_by('id')
    last_post = post_list[0]
    context = {
        'post_list': post_list,
        'last_post': last_post,
    }
    return render(request, 'blog/index.html', context)
