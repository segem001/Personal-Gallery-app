from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location,Category



def index(request):
    all_images=Image.objects.all()
    location=Location.objects.all()
    context={"all_images":all_images,"locations":location}
    return render(request,'app/index.html',context)

def search_results(request):
        if 'query'in request.GET and request.GET["query"]:
            search_term = request.GET.get("query")
            searched_articles = Image.search_image(search_term)
            message = f"{search_term}"

            return render(request, 'app/search.html',{"message":message, "articles":searched_articles})

        else:
            message= "You havent searched for any term"
            return render(request,'app/search.html',{"message":message})