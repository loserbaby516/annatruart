from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import ArtPiece, Description
# Create your views here.

def index(request):
    artpieces = ArtPiece.objects.all()
    return render(request, "portfolio/index.html", {
        "artpieces": artpieces,
        "format": "masonry-with-columns",
    })

def about(request):
    return render(request, "portfolio/about.html", {
        "format": "about",
    })

def contact(request):
    return render(request, "portfolio/contact.html", {
        "format": "contact",
    })

def full_view(request, artpiece):
    try:
        artpiece = ArtPiece.objects.get(preview_pic=artpiece)
    except ArtPiece.DoesNotExist:
        artpiece = ArtPiece.objects.get(full_pic=artpiece)
    if artpiece.full_pic:
        with open(artpiece.full_pic.path, 'rb') as f:
            image_data = f.read()
        return HttpResponse(image_data, content_type="image/jpeg")
    elif artpiece.preview_pic:
        with open(artpiece.preview_pic.path, 'rb') as f:
            image_data = f.read()
        return HttpResponse(image_data, content_type="image/jpeg")
    else:
        return HttpResponse("Image not found", status=404)
    
def info(request, id):
    artpiece = ArtPiece.objects.get(pk=id)
    return render(request, "portfolio/info.html", {
        "format": "about",
        "artpiece": artpiece,
    })