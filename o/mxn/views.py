from django.shortcuts import render, redirect

from .models import Morty
from .forms import CommentForm


def index(request):
    mortyz = Morty.objects.order_by('-date_added')

    context = {'mortyz': mortyz}

    return render(request, 'mxn/index.html', context)


def sign(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = Morty(name=request.POST['name'], commont=request.POST['comment'])
            new_comment.save()
            return redirect('index')

    else:
        form = CommentForm()

    context = {'form' : form}
    return render(request, 'mxn/sign.html', context)
