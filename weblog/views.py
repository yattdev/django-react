from django.shortcuts import render
from weblog.models import Post
from django.views.generic import ListView

# Create your views here.


class PostList(ListView):
    model = Post
    template_name = "post_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()

        return context
