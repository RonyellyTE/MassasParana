from django.urls import path
from .views import IndexView, LoginView, RegisterView, PasswordResetView, ProfileView, HomepageView, LogoutUserView, editar_cliente

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('homepage/', HomepageView.as_view(), name='homepage'),
    path('editar_cliente/', editar_cliente, name='editar_cliente')
]
