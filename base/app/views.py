from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post, User

# Create your views here.
def index(request):
    all_posts = Post.objects.all()  
    return render(request, 'app/index.html', {
        'posts': all_posts
    })

def add(request):
    if request.method == "POST":
        description = request.POST['description']
        images = request.FILES['image']
        catagory = request.POST['category']

        new_add = Post(
            user = User.objects.get(username = request.user),
            description = description,
            catagory = catagory,
            photo = images
        )
        new_add.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'app/add.html')