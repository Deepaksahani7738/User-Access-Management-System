from django.urls import path
from .views import index
from .views import add_data
from .views import view_data
from .views import main_data
from .views import post_edit
from .views import post_delete
from .views import register
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',index.as_view(),name='home'),
    path('add_data/',add_data.as_view(),name='add_data'),
    path('view_data/',view_data.as_view(),name='view_data'),
    path('post_detail/<int:pk>/',login_required(main_data.as_view()),name='post_detail'),
    path('post/delete/<int:pk>/',post_delete.as_view(),name='post_delete'),
    path('post/edit/<int:pk>/',post_edit.as_view(),name='post_edit'),
    path('login/',auth_views.LoginView.as_view(template_name='myapp/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='myapp/logout.html'),name='logout'),
    path('register/',register.as_view(),name='register'),
]
