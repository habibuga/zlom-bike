from django.shortcuts import render
from django.views import View

from .forms import SearchOffer


class StartView(View):
    def get(self, request):
        form = SearchOffer()
        return render(request=request, template_name="start_page.html", context={"form": form})

    def post(self, request):
        pass


