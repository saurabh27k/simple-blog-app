from django.urls import path
from . import views

app_name = "blogapp"

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('login/', views.login_view, name='login'),       # 👈 new
    path('logout/', views.logout_view, name='logout'),    # 👈 new
]

