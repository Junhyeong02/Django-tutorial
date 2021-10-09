from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def blog(request):
    postlist = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist':postlist})

def postdetails(request, pk):
    postlist = Post.objects.get(pk=pk)
    return render(request, 'main/postdetails.html', {'postlist':postlist})

def new_post(request):
    if request.method == 'POST':
        new_article = Post.objects.create(
            postname = request.POST['postname'],
            contents = request.POST['contents'],
            mainphoto = request.POST['mainphoto'],
        )

        return redirect('/blog/')
    return render(request, 'main/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk = pk)
    if request.method == "POST":
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})

