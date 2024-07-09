from django.shortcuts import render
from django.core.cache import cache
from pytube.contrib.search import Search
from .utils import search_youtube_resources
from .forms import SearchForm
from .models import SearchQueries

def home(request):
    form = SearchForm()
    data = []

    if "next" in request.GET.keys():
        res = request.session.get("res_data", None)
        if res:
            print(res)
        print("no cache")

    if request.method=="POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query=form.cleaned_data["query"]
            res = Search(query = query).results
            for d in res:
                title = d.title
                video_url = d.watch_url
                thumbnail = d.thumbnail_url
                rs_obj = {"title": title, "video_url": video_url, "thumbnail": thumbnail}
                data.append(rs_obj)
    print(data)
    return render(request=request, template_name="core/home.html", 
                  context={"form": form, "data": data})