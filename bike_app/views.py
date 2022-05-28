from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView

from .forms import SearchOffer
from .models import Offer, Category


class StartView(View):
    def get(self, request):
        form = SearchOffer()
        return render(request=request, template_name="start_page.html", context={"form": form})

    def post(self, request):
        pass


class OfferDetailView(DetailView):

    model = Offer
    template_name = "offer_details.html"
    context_object_name = "offer"


class CategoryContainView(View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        offers = Offer.objects.filter(category=category)
        ctx = {"offers": offers,
               "category": category}
        return render(request=request, template_name="category_content.html", context=ctx)
