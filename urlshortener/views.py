from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .forms import LinkShortForm
from .models import ShortedLink
from full_url.grabber import RequestGrabber
# Create your views here.


def index(request):
    links_data = None

    gr = RequestGrabber(request)
    domain = gr.protocol()+gr.domain()

    if request.user.is_authenticated:
        links_data = ShortedLink.objects.filter(owner=request.user)
    return render(request, 'index.html',
                  {
                      "links_data": links_data,
                      "domain": domain
                  })


def short_link(request):
    if request.method == "POST":
        form = LinkShortForm(request.POST)
        if form.is_valid():
            sl = form.save(commit=False)
            if request.user.is_authenticated:
                sl.owner = request.user
            sl.save()
            return JsonResponse({
                "success": True,
                "link": sl.short_link
            })
        else:
            print(form.errors)
            return JsonResponse({
                "success": False
            })


def use_link(request, link_hash):
    sl = get_object_or_404(ShortedLink, short_link=link_hash)
    return redirect(sl.original_link)
