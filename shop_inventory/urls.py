"""shop_inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('user', views.user),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    #Items
    path('user_items', views.user_items),
    path('show_items', views.show_items),
    path('edit_items/<int:id>', views.edit_items),
    path('update_items/<int:id>', views.update_items),
    path('delete_items/<int:id>', views.delete_items),

    #sales
    path('user_catsales', views.user_catsales),
    path('show_catsales', views.show_catsales),
    path('delete_catsales/<int:id>', views.delete_catsales),
]
