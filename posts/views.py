from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    """
    Post List View for displaying data.
    ListView: 'Render some list of objects'
    """
    model = Post
    template_name = 'home.html'
