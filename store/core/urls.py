from .views import HomeView
from user import views
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('login/', views.sign_in, name='login'),
    path('login/register/', views.sign_up, name='register'),
    path('page_user/', views.page_user, name='user'),
    path('logout/', views.logout_view, name='logout'),
]

