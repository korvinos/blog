from django.shortcuts import render
from django.http import HttpResponse
from models import Post

# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request):
    post_list = Post.objects.order_by('created')
    context = {
        'post_list': post_list
    }
    return render(request, 'blog/index.html', context)
