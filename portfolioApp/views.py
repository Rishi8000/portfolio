from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def home(request):
    # print(request.resolver_match.url_name)
    # context = {'page': ' - Welcome to my Portlfoilo!','id':'home'}
    service_list = [
        {
            "icon": "fa-solid fa-code fa-8x fa-fw",
            "title": "Frontend Development",
            "description": "Specialize in responsive and interactive front-end development using modern technologies."
        },
        {
            "icon": "fa-solid fa-gears fa-8x fa-fw",
            "title": "Backend Development",
            "description": "Building a scalable, secure and maintainable backend for your web application."
        },
        {
            "icon": "fa-brands fa-python fa-7x fa-fw",
            "title": "Python Programming",
            "description": "Expertise in developing scalable and maintainable applications using Python, with a focus on efficiency and readability."
        }
    ]
    return render(request, 'home.html', {'services': service_list})


def skills(request):
    print(request.resolver_match.url_name)
    context = {'page': ' | My Skills','id':'skills'}
    # template = loader.get_template('skills.html')
    # return HttpResponse(template.render(context=context))
    return render(request, 'skills.html')


def aboutMe(request):
    print(request.resolver_match.url_name)
    context = {'page': ' - About Me','id':'aboutMe'}
    # template = loader.get_template('about.html')
    # return HttpResponse(template.render(context=context))
    return render(request, 'about.html')


def contact(request):
    print(request.resolver_match.url_name)
    context = {'page': ' - Contact','id':'contact'}
    # template = loader.get_template('contact.html')
    # return HttpResponse(template.render(context=context))
    return render(request, 'contact.html')