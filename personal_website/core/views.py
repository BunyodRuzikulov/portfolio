from django.shortcuts import render, redirect
from .models import Project, BlogPost, ContactMessage, Skill, Service, WorkExperience, Education, Certificate,Profile
from django.contrib import messages

def home(request):
    projects = Project.objects.all()[:3]
    posts = BlogPost.objects.all()[:3]
    return render(request, 'index.html', {'projects': projects, 'posts': posts})

def about(request):
    skills = Skill.objects.all()
    return render(request, 'about.html', {'skills': skills})

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def blog_detail(request, pk):
    post = BlogPost.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'post': post})

def resume(request):
    skills = Skill.objects.all().order_by('-percentage')
    work_experiences = WorkExperience.objects.all().order_by('-start_date')
    educations = Education.objects.all().order_by('-start_date')
    certificates = Certificate.objects.all().order_by('-issue_date')
    profile = Profile.objects.first()  # Faqat bitta profil rasmi
    return render(request, 'resume.html', {
        'skills': skills,
        'work_experiences': work_experiences,
        'educations': educations,
        'certificates': certificates,
        'profile': profile
    })

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        ContactMessage.objects.create(name=name, email=email, message=message)
        messages.success(request, "Xabar yuborildi!")
        return redirect('contact')
    return render(request, 'contact.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})