
from django.conf.urls.static import static
from django.urls import path
from digi.settings import STATIC_URL
from django.conf import settings

from . import views

from django.conf import settings

urlpatterns = [ 
       path('', views.index, name='index'),
    path('login/', views.login, name='login'),
       path('logout/', views.signout, name='logout'),
        path('signup/', views.signup, name='signup'),
        path('authoritaire/', views.authoritaire, name='authoritaire'),
        path('client/', views.client, name='client'),
        path('import-file/', views.import_file, name='import_file'),
        path('demande/', views.demande, name='demande'),
        path('hello-cl/', views.hello_cl, name='hello_cl'),
        path('hello-autho/', views.hello_autho, name='hello_autho'),
        path('import_file/', views.import_file, name='import_file'),
        path('list/', views.list_files, name='list_files'),

         ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

