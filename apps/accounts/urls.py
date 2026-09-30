from django.urls import path
from apps.accounts.views import LoginView, LogoutView, RegisterView, ProfileView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login',),
    path('logout/', LogoutView.as_view(), name='logout',),
    path('registration/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile')
]