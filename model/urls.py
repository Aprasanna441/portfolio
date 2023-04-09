from model import views
from django.urls import path,include
from model.views import SkillView,ProjectView,AboutView,ContactView,CategoricalView
urlpatterns = [
    
    path('',AboutView.as_view(),name="about"),
    path('my-skills',SkillView.as_view(),name="skills"),
    path('my-projects',ProjectView.as_view(),name="projects"),
    path('contact-me',ContactView.as_view(),name="contact"),
    path('categorical/<int:d>/',CategoricalView.as_view(),name="categorical"),

]