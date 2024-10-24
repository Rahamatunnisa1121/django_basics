from django.urls import path
from . import views

urlpatterns=[
    path('hello/',views.say_hello),
    #as playgriund is added in the url in storefront.urls, only hello with a forward slash is added in route
]