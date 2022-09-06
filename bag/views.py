from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)

# Create your views here.
def view_bag(request):
    '''
    A view to return the bag page
    '''
    return render(request, 'bag/bag.html')
