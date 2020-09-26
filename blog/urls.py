from django.urls import path
from .  import views
from .views import  PostListView, PostDetailView, PostCreateView, PostUpdateeView, PostDeleteView,UserPostListView

urlpatterns = [
    path('',PostListView.as_view(),name='blogs-home'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-blogs'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update/',PostUpdateeView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('post/create/',PostCreateView.as_view(),name='post-create'),
    path('about/',views.about,name='blogs-about'),
]
