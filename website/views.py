from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def home(request):

    links = {
        'linkedin' : 'https://www.linkedin.com/in/ragavi-dr',
        'github' : 'https://github.com/ragavi-dr',
        'gfg' : 'https://www.geeksforgeeks.org/user/ragavila0z',
    }

    education = [
        {'degree': 'BCA', 'college' : 'St.Theresa Arts and Science College', 'Affiliation' : 'Annamalai University', 'batch' : '2023-2026', 'cgpa':'9.2/10'},
    ]

    certifications = [
        {'name' : 'TCS ion Career Egde Young Professionals', 'issuer' : 'TCS ion'},
        {'name' : 'Introduction to SQL', 'issuer' : 'Infosys Springboard'},
    ]

    activity = [
        {'platform' : 'GeekeforGeeks', 'stat': '60+ problems solved', 'link' : links['gfg']},
        {'platform' : 'GitHub', 'stat': 'Python, Django, HTML and CSS Projects', 'link': links['github']},
    ]

    projects = [
        {
            'title' : 'Portfolio Website',
            'description' : 'Designed and developed a responsive portfolio website to showcase my skills, projects, achievements and professional profile.',
            'techstacks' : 'Django, Bootstrap, HTML, CSS',
            'repo' : 'https://github.com/ragavi-dr/Django-Portfolio.git/',
        },
        {
            'title' : 'Student Perfomance Analysis System',
            'description' : 'Designed a centralised MySQL Database to manage and analyse student records, attendence, marks and perfomance trends.',
            'techstacks' : 'SQL, MySQL',
            'repo' : '#',
        },
        {
            'title' : 'Retail Sales Analysis System',
            'description' : 'Cleaned and analyzed retail sales data to identify business trends and generated key insights',
            'techstacks' : 'Python, Pandas, Numpy',
            'repo' : '#'
        },
    ]

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            try:
                EmailMessage(
                    subject=f'Portfolio message from {msg.name}',
                    body = f'Name: {msg.name}\nEmail: {msg.email}\n\n{msg.message}',
                    from_email=settings.EMAIL_HOST_USER,
                    to=[settings.EMAIL_HOST_USER],
                    reply_to=[msg.email],
                ).send()
            except Exception as e:
                print("EMAIL ERROR:",e)
            messages.success(request, 'Thanks! Your message was sent. You will get your response soon..')
            return redirect('/#contact')
    else:
        form = ContactForm()

    return render(request, 'home.html', {
        'links' : links,
        'education' : education,
        'certifications': certifications,
        'projects':projects,
        'activity' : activity,
        'form' : form,})