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
    # print(request.resolver_match.url_name)
    # context = {'page': ' | My Skills','id':'skills'}
    # # template = loader.get_template('skills.html')
    # # return HttpResponse(template.render(context=context))
    # return render(request, 'skills.html')
    skills = {
        "Programming Languages": [
            {"name":"Python","icon":"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/640px-Python-logo-notext.svg.png"},
            {"name":"PHP","icon":"https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/PHP-logo.svg/1200px-PHP-logo.svg.png"},
            {"name": "C", "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/C_Programming_Language.svg/695px-C_Programming_Language.svg.png"},
            {"name":"Java","icon":"https://education.oracle.com/file/general/p-80-java.png"},
            {"name": "Java Script", "icon": "https://icons.veryicon.com/png/o/business/vscode-program-item-icon/javascript-3.png"},
            {"name": "SQL", "icon": "https://uxwing.com/wp-content/themes/uxwing/download/web-app-development/database-icon.png"},
            # Add other programming languages here
        ],
        "Front-end": [
            {"name": "HTML", "icon": "https://kinsta.com/wp-content/uploads/2021/03/HTML-5-Badge-Logo.png"},
            {"name": "CSS", "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/CSS3_logo.svg/800px-CSS3_logo.svg.png"},
            {"name": "Java Script", "icon": "https://icons.veryicon.com/png/o/business/vscode-program-item-icon/javascript-3.png"},
            {"name": "Bootstrap", "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Bootstrap_logo.svg/640px-Bootstrap_logo.svg.png"},            
            # Add other front-end skills here
        ],
        "Back-end": [
            {"name":"PHP","icon":"https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/PHP-logo.svg/1200px-PHP-logo.svg.png"},
            {"name": "Django", "icon": "https://static-00.iconduck.com/assets.00/django-icon-1606x2048-lwmw1z73.png"},
            {"name": "Flask", "icon": "https://static-00.iconduck.com/assets.00/programming-language-flask-icon-2048x1826-wf5k5ugs.png"},
            {"name": "SQL", "icon": "https://uxwing.com/wp-content/themes/uxwing/download/web-app-development/database-icon.png"},
            
            # Add other back-end skills here
        ],
        "Other Tools": [
            {"name": "Git", "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Git_icon.svg/2048px-Git_icon.svg.png"},
            {"name": "GitHub", "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/GitHub_Invertocat_Logo.svg/1200px-GitHub_Invertocat_Logo.svg.png"},
            {"name": "VSCode", "icon": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png"},
            # Add other tools here
        ],
    }
    return render(request, 'skills.html', {'skills': skills})



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