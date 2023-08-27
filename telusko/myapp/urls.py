from django.urls import path

from myapp import views


urlpatterns = [
    path('calc/',views.home, name = 'home'),
    path('calculation/', views.calculation, name="calculation"),
    # path('divO/', views.divO, name = 'divO')
    



]