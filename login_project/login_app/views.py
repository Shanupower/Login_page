from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import User
from .models import Post
from .models import Post
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post
import os
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
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

def view_posts(request):
    posts = Post.objects.all()
    return render(request, 'viewposts.html', {'posts': posts})
    
def login_submit(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate the user
            try:
                user = User.objects.get(username=username, password=password)
                # Perform login operation (e.g., store user ID in session)
                return redirect('success.html')  # Redirect to the dashboard page
            except User.DoesNotExist:
                pass

    return redirect('login')  # Redirect back to the login page if authentication fails

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

