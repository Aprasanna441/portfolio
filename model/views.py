from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Skills,Projects

# Create your views here.






class AboutView(TemplateView):
    template_name="about.html"


class SkillView(TemplateView):
    template_name="skills.html"
    def get_context_data(self, **kwargs):
        skills=Skills.objects.all()
        context={'skills':skills}
        return context


class ProjectView(TemplateView):
    template_name="projects.html"
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        projects=Projects.objects.all()
        cate=Skills.objects.filter(relevant=True)
        context['projects']=projects
        context['cate']=cate
        return context

        


class ContactView(TemplateView):
    template_name="contact.html"

class CategoricalView(TemplateView):
    template_name="projects.html"
    
    def get_context_data(self, **kwargs):
        cate=Skills.objects.filter(relevant=True)
        d=self.kwargs['d']
        skill=Skills.objects.get(id=d)

        projects=Projects.objects.filter(category=skill)
        
        context={'projects':projects,'cate':cate}
        return context

    
    

