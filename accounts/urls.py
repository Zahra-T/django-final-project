from django.urls import path
from django.contrib.auth import views as auth_views
from . views import signup, logout
app_name='accounts'
urlpatterns=[
    path('login/', auth_views.LoginView.as_view
    (template_name='accounts/signup_login.html', redirect_field_name='next'), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout')
]
