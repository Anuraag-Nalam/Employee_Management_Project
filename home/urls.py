from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    
    path('',views.ouremp,name="ouremp"),
    path('addemp',views.addemp,name="addemp"),
    path('editemp',views.editemp,name="editemp"),
    path('viewemp',views.viewemp,name="viewemp"),
    path('delete/<int:id>',views.delete,name='delete')

]
