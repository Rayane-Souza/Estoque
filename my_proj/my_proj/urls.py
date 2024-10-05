from django.urls import path, include
from django.shortcuts import redirect
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    path('', lambda request: redirect('produto_list')),  
]
