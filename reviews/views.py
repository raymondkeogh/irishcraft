# Views for Edit Review, Add Review and Delete Review
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ObjectDoesNotExist

from .forms import ReviewForm
from .models import Review
from products.models import Product


# I fount this tutorial very helpful when creating the Review view
# https://www.codementor.io/@jadianes/get-started-with-django-building-recommendation-review-app-du107yb1a
@login_required
def add_review(request, product_id):
    """ Review a product """
    product = get_object_or_404(Product, pk=product_id)
    try:
        review = Review.objects.get(user=request.user)
    except ObjectDoesNotExist:
        review = None
    if review is not None:
        form = ReviewForm(instance=review)
        messages.info(
            request, f'You are editing your review for {review.product}')

        template = 'reviews/edit_review.html'
        context = {
            'form': form,
            'review': review,
        }
        return render(request, template, context)

    else:
        form = ReviewForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                title = form.cleaned_data['title']
                body = form.cleaned_data['body']
                rating = form.data['rating']
                user = request.user
                review = Review()
                review.product = product
                review.title = title
                review.body = body
                review.user = user
                review.rating = rating
                review.save()
                messages.success(
                        request, 'Your review has been uploaded!')

                return redirect(reverse('product_details', args=[product.id]))
            else:
                messages.error(
                    request, 'Failed to upload product review. '
                    'Please ensure the review form is filled correctly.')
        else:
            form = ReviewForm()
        template = 'reviews/add_review.html'
        context = {
            'form': form,
            'product': product
        }

        return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """ A view to edit review details """
    review = get_object_or_404(Review, pk=review_id)

    if request.user != review.user:
        messages.error(
            request, "You must have shop Superuser access in order to"
            "add a product, please contact you web adminstrator in"
            "order to set up the correct permissions to access this function")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review Updated!')
            return redirect(
                reverse('product_details', args=[review.product.id]))
        else:
            messages.error(request, 'There was a problem updating your review'
                           ', please check to see if all'
                           'the details have been filled in correctly')
    else:
        form = ReviewForm(instance=review)
        messages.info(
            request, f'You are editing your review for {review.product}')

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ A view to delete a product review """
    review = get_object_or_404(Review, pk=review_id)

    review.delete()
    messages.success(request, 'Your review has been deleted!')
    return redirect(reverse('products'))
