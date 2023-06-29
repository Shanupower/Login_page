from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, UserForm, NewsForm
from .models import User, UserModel
from .models import NewsModel
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import NewsModel
import os
import pymongo
from django.conf import settings

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

# connect_string = 'mongodb://<root>:<root>@localhost/dummy?retryWrites=true&w=majority' 
# my_client = pymongo.MongoClient(connect_string)

# # First define the database name
# dbname = my_client['dummy']

# collection_name = dbname["news"]


@csrf_exempt
def news_list(request):
    if request.method == 'GET':
        news = Post.objects.all()
        data = []
        for n in news:
            news_data = {
            'id': n.id,
            'title': n.title,
            'content': n.content,
            'author': n.author,
            'tags': n.tags,
            'core_categories': n.core_categories,
            'created_at': n.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'img': n.img.url if n.img else ''
            }
            data.append(news_data)
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        content = data.get('content')
        author = data.get('author')
        tags = data.get('tags')
        core_categories = data.get('core_categories')
        img = data.get('img')

        post = Post.objects.create(
            title=title,
            content=content,
            author=author,
            tags=tags,
            core_categories=core_categories,
            img=img
        )

        response_data = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author': post.author,
            'tags': post.tags,
            'core_categories': post.core_categories,
            'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'img': post.img.url if post.img else ''
        }

        return JsonResponse(response_data, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
def login_view(request):
    form = UserForm()
    return render(request, 'login.html', {'form': form})

def view_posts(request):
    posts = NewsModel.objects.all()
    return render(request, 'viewposts.html', {'posts': posts})

def login_submit(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
        return render(request, "success.html")
    context = {}
    return render(request, 'accounts/signin.html', context)

def get_user(request):
    if request.method == 'GET':
        users = User.objects.all()
        data = []
        for n in users:
            news_data = {
            'name': str(n.first_name) + " " + str(n.last_name),
            'emailId': n.email
            }
            data.append(news_data)
        return JsonResponse(data, safe=False)
    
@csrf_exempt
def delete_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        # fetch the user object and delete it
        user = User.objects.get(email=email)
        user.delete()
        return JsonResponse({"result":"deleted"}, safe=False)
    else:
        return JsonResponse({"result": "Sorry you aren't allowed."}, safe=False)


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False,)
            user.is_active = True
            user.save()
            return render(request, 'success.html')
        else:
            return render(request, 'error.html')
    
    else:
        return render(request, 'accounts/signup.html')

@csrf_exempt
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST or None)
        if form.is_valid():
            print("here")
            form.save()
            return JsonResponse({"result": "success"}, safe=False)
        else:
            return JsonResponse({"result": "failed to upload"}, safe=False)
    else:
        return JsonResponse({"result": "Sorry you aren't allowed."}, safe=False)


# def save_post(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         content = request.POST['content']
#         author = request.POST['author']
#         tags = request.POST['tags']
        
#         post = Post(title=title, content=content, author=author, tags=tags)
#         post.save()
#         return redirect('post_success')

#     return render(request, 'form.html')

# def post_success(request):
#     return render(request, 'success.html')


def view_top_news_category(request):
    # create a view to display latest 10 top news category wise using the category get parameter
    category = request.GET.get('category')
    #check if category is present in the request
    if category:
        # if present, filter the news based on the category
        news = NewsModel.objects.filter(category=category).order_by('-created_at')[:10]
    else:
        # if not present, display all the news
        news = NewsModel.objects.all().order_by('-created_at')[:10]
    # render the viewposts.html template with the news
    return render(request, 'viewposts.html', {'posts': news})

