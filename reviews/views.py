from django.shortcuts import redirect, render
from .forms import ReviewForm

# Create your views here.
def create(req):
    if req.method == 'POST':
        form = ReviewForm(req.POST)

        if form.is_valid():
            form.save()

            return redirect('reviews:index')

    else:
        form = ReviewForm()

    context = {
        'form': form
    }

    return render(req, 'reviews/create.html', context)