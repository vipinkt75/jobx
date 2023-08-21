from django.urls import path
from . import views
from .views import JobDetailView
from .views import UserProfileView, UserProfileUpdateView


app_name = "web"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("contact/", views.Form.as_view(), name="contact"), 
    path("job-list/", views.jobLists.as_view(), name="job-list"),
    path('job-detail/<int:pk>/', views.JobDetailView.as_view(), name='job-detail'),
    path("about/", views.about.as_view(), name="about"),
    path("category/", views.category.as_view(), name="category"),
    path("testimonial/", views.testimonial.as_view(), name="testimonial"),
    path("postjob/", views.postjob.as_view(), name="postjob"),
    path("search/", views.SearchListView.as_view(), name="search"),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/update/<int:pk>/', UserProfileUpdateView.as_view(), name='profile_update'),
    
]