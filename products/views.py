from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm

# Create your views here.
def all_products(request):
    """
    A view to display all products
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)


        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            selected_categories = request.GET.get('category')


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'No product found')
                return redirect(reverse('products'))
            
            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view with product details
    """
    products = Product.objects.all()
    product = get_object_or_404(Product, pk=product_id)

    liked = False
    if product.likes.filter(id=request.user.id).exists():
        liked = True
    
    if request.method == 'POST':

        review_form = ReviewForm(data=request.POST or None)

        if request.user.is_authenticated and review_form.is_valid():

            review_form.instance.user = request.user
            review = review_form.save(commit=False)
            review.product = product
            review.save()
            messages.success(request, ('Thank you for your review!'))

            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Please login to create a review on one of our products!')
            return redirect(reverse('product_detail', args={product.id}))
    else:
        review_form = ReviewForm()

    reviews = Review.objects.filter(product=product)


    context = {
        'product': product,
        'products': products,
        'liked': liked,
        'reviews': reviews,
        'review_form': review_form,
    }

    return render(request, 'products/product_detail.html', context)