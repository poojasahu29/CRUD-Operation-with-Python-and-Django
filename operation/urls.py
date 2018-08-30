
from django.conf.urls import url
from .import views

urlpatterns = [
    url('^$',views.index,name="index" ),

    url(r'^create/$',views.create,name="create"),

    url(r'^add_book/$',views.add_book,name='add_book'),

    url(r'^delete/(?P<id>\d+)/$',views.delete,name="delete" ),

    url(r'^edit/(?P<id>\d+)/$',views.edit,name="edit" ),

    url(r'^update/(?P<id>\d+)/$',views.update,name='update'),
   
]
