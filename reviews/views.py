from django.shortcuts import redirect, render
from .forms import ReviewForm, CommentForm
from .models import Review, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create(req):
    if req.method == 'POST':
        form = ReviewForm(req.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.user = req.user
            data.save()

            return redirect('reviews:index')

    else:
        form = ReviewForm()

    context = {
        'form': form
    }

    return render(req, 'reviews/create.html', context)


@login_required
def index(req):
    data = Review.objects.all().order_by('id')

    return render(req, 'reviews/index.html', {'data': data})


@login_required
def detail(req, review_pk):
    data = Review.objects.get(id=review_pk)
    form = CommentForm()
    comments = Comment.objects.all()

    context = {
        'data': data,
        'form': form,
        'comments': comments
    }

    return render(req, 'reviews/detail.html', context)


@login_required
def update(req, review_pk):
    data = Review.objects.get(id=review_pk)

    if req.method == 'POST':
        form = ReviewForm(req.POST, instance=data)

        if form.is_valid():
            form.save()

            return redirect('reviews:detail')

    else:
        form = ReviewForm(instance=data)

    context = {
        'form': form
    }

    return render(req, 'reviews/create.html', context)


@login_required
def delete(req, review_pk):
    Review.objects.get(id=review_pk).delete()

    return redirect('reviews:detail')


@login_required
def comments_create(req, review_pk):
    data = Comment.objects.get(id=review_pk)
    form = CommentForm(req.POST)

    if form.is_valid():
        # 'commit=False' option means return instance don't be saved
        comment = form.save(commit=False)
        comment.review = data
        comment.user = req.user
        comment.save()

    return redirect('reviews:detail')
