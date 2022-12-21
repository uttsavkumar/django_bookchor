 
from django.contrib import admin
from django.urls import path
from .view import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insertpage/',insertpage,name='insert'),
    path('insertcat/',insertcategory,name='insertcat'),
    path('search/',searchbook,name='search'),
    path('singlecat/<int:id>',singlecat,name='singlecat'),
    path('view/<int:id>',singlepage,name='singlepage'),
    path('',home,name='home')
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)