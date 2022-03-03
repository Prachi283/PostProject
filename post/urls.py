from django.urls import path
from .views import PostPageView
urlpatterns = [

    path('posts/',PostPageView.as_view(),name='posts'),
   
]
