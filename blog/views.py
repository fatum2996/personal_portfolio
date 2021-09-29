from django.shortcuts import render
from .models import Blog_record

# Create your views here.
def all_blogs(request):
    blogs = Blog_record.objects.order_by('-data')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})
