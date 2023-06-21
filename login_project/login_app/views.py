from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import User
from .models import Post
from .models import Post


def login_view(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

def view_posts(request):
    posts = Post.objects.all()
    return render(request, 'view_posts.html', {'posts': posts})
    
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
                return redirect('dashboard')  # Redirect to the dashboard page
            except User.DoesNotExist:
                pass

    return redirect('login')  # Redirect back to the login page if authentication fails

def save_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        tags = request.POST['tags']
        
        post = Post(title=title, content=content, author=author, tags=tags)
        post.save()
        return redirect('post_success')

    return render(request, 'form.html')

def post_success(request):
    return render(request, 'success.html')

