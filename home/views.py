from django.shortcuts import render, redirect
from django.http import Http404
from datetime import datetime
from home.models import Contact
from home import catalog
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login


# Create your views here.
def index(request):
    featured = [category["products"][-1] for category in catalog.CATEGORIES[:3]]
    return render(request, 'home.html', {"featured": featured})


def about(request):
    return render(request, 'about.html')


def services(request, slug=None):
    query = request.GET.get('q', '').strip()
    context = {"query": query, "active_slug": slug}

    if query:
        context["results"] = catalog.search(query)
    elif slug:
        category = catalog.get_category(slug)
        if category is None:
            raise Http404("Category not found")
        context["sections"] = [category]
        context["page_title"] = category["name"]
    else:
        context["sections"] = catalog.CATEGORIES

    return render(request, 'services.html', context)


def familypack(request):
    # kept so old /familypack links still work
    return services(request, slug="family-packs")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
        # redirect so refreshing the page doesn't submit the form again
        return redirect("/contact")
    return render(request, 'contact.html')


def first(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return redirect("/")


def loginUser(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/")
