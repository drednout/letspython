from django.conf.urls import include, url
from django.contrib import admin
from base import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'form_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^change_player/([0-9]+)/', views.change_player),
    url(r'^change_player_django_form/([0-9]+)/', views.change_player_django_form),
    url(r'^player_changed/([0-9]+)/', views.player_changed),
]
