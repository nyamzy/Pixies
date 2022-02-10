from django.shortcuts import render, redirect
from .models import Image, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title = "Pixies"
    image_list = Image.objects.all()
    context = {
        "title": title,
        "image_list": image_list,
    }
    return render(request, "all-pix/index.html", context)


def search_results(request):
    if 'image' in request.GET and request.GET["article"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'all-pix/search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pix/search.html', {"message": message})