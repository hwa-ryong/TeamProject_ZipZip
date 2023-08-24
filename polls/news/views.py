from django.shortcuts import render

# Create your views here.
def news(request):
    return render(request, 'community/news/cardlist.html')