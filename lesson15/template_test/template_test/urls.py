from django.conf.urls import include, url
from django.contrib import admin

import base.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'template_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test1$', base.views.test1),
    url(r'^test2$', base.views.test2)
]
