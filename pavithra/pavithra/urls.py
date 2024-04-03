from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('surfaceareaofrightcylinder/',views.surfaceareaofrightcylinder,name="surfaceareaofrightcylinder"),
    path('',views.surfaceareaofrightcylinder,name="surfaceareaofrightcylinderroot")
]