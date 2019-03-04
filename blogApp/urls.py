from django.urls import path , include
from . import views


urlpatterns = \
    [
        # path('',views.logIn, name='login'),
        path('blogView/',views.index, name='index'),
    ]


urlpatterns += \
    [
        path('accounts/', include('django.contrib.auth.urls')),
    ]