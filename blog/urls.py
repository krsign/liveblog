from django.urls import path,include
from blog.views import  contact_us_form_view
from blog.views import  CategoryList, PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('category/<int:id>', CategoryList.as_view(), name='filter'),
    path('',PostListView.as_view(), name='home'),
    path('blog/<slug:slug>',PostDetailView.as_view(), name='post-detail'), 

    path('contact', contact_us_form_view, name='contact-us'),
    
    path('post', PostCreateView.as_view(), name='new-post'),
    path('post/<slug:slug>',PostUpdateView.as_view(), name='update'),
    path('delete/<slug:slug>',PostDeleteView.as_view(), name='delete'), 
    
]