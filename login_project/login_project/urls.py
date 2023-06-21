from django.contrib import admin
from django.urls import path
from login_app.views import login_view, login_submit
from login_app.views import save_post, post_success,view_posts




urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('view_posts/', view_posts, name='view_posts'),
    path('login_submit/', login_submit, name='login_submit'),
     path('save_post/', save_post, name='save_post'),
    path('post_success/', post_success, name='post_success'),
      
]

