from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.cache import cache
from django.contrib import messages
from pytube.contrib.search import Search
from .utils import request_youtube_resource, search_youtube_resources
from .forms import SearchForm, DownloadForm

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
    return render(request=request, template_name="core/home.html", 
                  context={"form": form, "data": data})

def show_available_download(request):
    form = DownloadForm()
    audios_dict = {}
    videos_dict = {}
    if request.method == "POST":
        form = DownloadForm(request.POST)
        try:
            count = 0
            if form.is_valid():
                link = form.cleaned_data["yt_link"]
                if cache.get(f"{link}_audios") or cache.get(f"{link}_videos"):
                    print("from cache")
                    audios = cache.get(f"{link}_audios")
                    videos = cache.get(f"{link}_videos")
                    thumbnail = cache.get(f"{link}_thumbnail")
                else:
                    print("From API")
                    audios, videos, thumbnail_url = request_youtube_resource(
                        link)
                    cache.set(f"{link}_audios", audios)
                    cache.set(f"{link}_videos", videos)
                    thumbnail = cache.set(f"{link}_thumbnail", thumbnail_url)
                for audio in audios:
                    audios_dict[f"{count}_audio"] = {
                        "type": audio.type,
                        "size": audio.filesize_mb,
                        "quality": audio.abr,
                        "item": str(audio)
                    }
                    count = count + 1
                for video in videos:
                    title = video.title
                    if video.resolution in ["360p", "1080p",
                                            "720p", "480p"]:
                        videos_dict[f"{count}_video"] = {
                            "type": video.mime_type,
                            "size": video.filesize_mb,
                            "quality": video.resolution,
                            "item": str(video)
                        }
                        count = count + 1
                return render(request, "core/download.html", {'form': form, 
                                                              "audios": audios_dict, 
                                                              "videos": videos_dict,
                                                              "title": title,
                                                              "thumbnail": thumbnail})
        except Exception as e:
            messages.error(request, str(e))
            return redirect("show_available_download")

    return render(request=request, template_name="core/download.html", context={'form': form,
                                                                                "audios": audios_dict,
                                                                                "videos": videos_dict})


def download(request):
    pass