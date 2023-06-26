from django.shortcuts import render, redirect
from .forms import UserForm
from .models import UserModel
from .models import PostModel
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PostModel
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
    posts = PostModel.objects.all()
    return render(request, 'viewposts.html', {'posts': posts})
    
def login_submit(request):
    if request.method == 'POST':
        
        form = UserForm(request.POST or None)
        if form.is_valid():
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            form.save()
            # Authenticate the user
            # try:
            #     user = User.objects.get(username=username, password=password)
            #     print(user)
            #     form.save()
            #     # Perform login operation (e.g., store user ID in session)
            return render(request, "success.html")  # Redirect to the dashboard page
            # except User.DoesNotExist:
            #     print("in except")
    return redirect('login')  # Redirect back to the login page if authentication fails

def get_user(request):
    if request.method == 'GET':
        users = UserModel.objects.all()
        data = []
        for n in users:
            news_data = {
            'name': n.name,
            'emailId': n.emailId
            }
            data.append(news_data)
        return JsonResponse(data, safe=False)
    
@csrf_exempt
def delete_user(request):
    if request.method == "DELETE":
        id = "64996ba5e943b1f37fc2ba3a"
        print(id)
        print('here')
        # fetch the object related to passed id
        obj = get_object_or_404(UserModel, id = id)
        obj.delete()
        # # pass the object as instance in form
        # form = UserForm(request.POST or None, instance = obj)
    
        # # save the data from the form and
        # # redirect to detail_view
        # if form.is_valid():
        #     form.save()
        return JsonResponse({"result":"deleted"}, safe=False)


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST or None)
        if form.is_valid():
            print("here")
            form.save()
            return JsonResponse({"result": "success"}, safe=False)
        else:
            return render(request, "success.html")


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

