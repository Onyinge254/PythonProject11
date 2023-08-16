from django.urls import path
from .views import Teamleader_dashboard,default_landing_page,signup
from django.contrib.auth.views import LoginView,LogoutView


app_name = 'CAL_INSIGHTS'

urlpatterns = [
    path('', default_landing_page, name='default_landing_page'),
    path('dashboard/Teamleader/', Teamleader_dashboard, name='Teamleader_dashboard'),

    # Authentication URLs
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),

    # Other URL patterns
]