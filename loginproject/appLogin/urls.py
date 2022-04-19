from django.urls import include, re_path
from appLogin import views
# SET THE NAMESPACE!
app_name = 'appLogin'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^user_login/$',views.user_login,name='user_login'),
]