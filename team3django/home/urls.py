from django.contrib import admin
from django.conf.urls import url
from . import views
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('',views.index, name = 'index'),
    #url(r'^admin/', admin.site.urls),
    url(r'^$',views.signIn),
    url(r'^postsign/',views.postsign),
    url(r'^logout/',views.logout,name="log"),
    url(r'^signup/',views.signUp,name='signup'),
        url(r'^postsignup/',views.postsignup,name='postsignup'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    #url(r'^', include('home.urls', namespace='home')),
]
