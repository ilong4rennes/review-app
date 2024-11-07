from django.shortcuts import get_object_or_404, render, redirect
from .models import User, Business, Review
from .forms import ReviewForm

def user_index(request):
    users = User.objects.all()
    return render(request, 'reviewmaster/user_index.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    rated_businesses = user.rated_businesses()
    content_based_recommended_businesses = user.content_based_recommended_businesses()
    collaborative_based_recommended_businesses = user.collaborative_based_recommended_businesses()
    return render(
        request,
        'reviewmaster/user_detail.html',
        {
            'user': user,
            'rated_businesses': rated_businesses,
            'content_based_recommended_businesses': content_based_recommended_businesses,
            'collaborative_based_recommended_businesses': collaborative_based_recommended_businesses
        }
    )

def business_index(request):
    businesses = Business.objects.all()
    return render(request, 'reviewmaster/business_index.html', {'businesses': businesses})

def business_detail(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    return render(request, 'reviewmaster/business_detail.html', {'business': business})

def review_list(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    reviews = Review.objects.filter(business=business)
    return render(request, 'reviewmaster/review_list.html', {'business': business, 'reviews': reviews})

def review_create(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.business = business
            review.save()
            return redirect('business_detail', business_id=business.id)
    else:
        form = ReviewForm()
    return render(request, 'reviewmaster/review_form.html', {'form': form, 'business': business})
