from django.contrib import admin
from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HOME, name='home'),
    path('contact/', views.CONTACT, name='contact'),
    path('login/', views.LOGIN, name='login'),
    path('register/', views.REGISTER, name='register'),
    path('single_post/<slug:slug>/', views.SINGLE_POST, name='single_post'),
    path('my_posts/', views.MY_POSTS, name='my_posts'),
    path('new_post/', views.NEW_POST, name='new_post'),
    path('edit_post/<int:id>/', views.EDIT_POST, name='edit_post'),
    path('delete_post/<int:id>/', views.DELETE_POST, name='delete_post'),

    path('fetchmobile/', views.FETCH_MOBILE,name='fetchmobile'),
    path('fetchmobilelogin/', views.FETCH_MOBILE_LOGIN,name='fetchmobilelogin'),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
