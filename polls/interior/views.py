from django.shortcuts import render

# Create your views here.
def board_interior(request):
    return render(request, 'community/board_interior/board_interior.html')