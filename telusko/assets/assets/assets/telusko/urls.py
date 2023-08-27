
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('calc/', include('myapp.urls')),
    path('', include('travelloo.urls')),

    path('admin/', admin.site.urls),

]
