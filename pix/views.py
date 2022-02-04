from django.shortcuts import render

# Create your views here.
def home(request):
    title = "Pixies"
    context = {
        "title": title,
    }
    return render(request, "all-pix/index.html", context)