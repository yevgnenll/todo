from django.conf.urls import url
from django.contrib import admin

from todo.views import home
from lists.views import view_list, new_list


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^lists/the-only-list-in-the-world/$', view_list, name="only"),
    url(r'^lists/new/$', new_list, name="new"),

]
