import pathlib
import tempfile
from django.shortcuts import render
from pathlib  import Path
from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse
from django.core.cache import cache
from django.contrib import messages
from pytube.contrib.search import Search
from .utils import load_fetched_data
from .forms import SearchForm, DownloadForm
from pathlib import Path
import os
from django.http import FileResponse

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
                url_link = link.split("/")[-1]
                audios, videos, thumbnail, link = load_fetched_data(link)
                for audio in audios:
                    audios_dict[f"{count}_audio"] = {
                        "type": str(audio.type),"size": audio.filesize_mb,
                        "quality": audio.abr, "item": audio
                    }
                    count = count + 1
                for video in videos:
                    title = video.title
                    if video.resolution in ["360p", "720p", "480p"]:
                        videos_dict[f"{count}_video"] = {
                            "type": str(video.mime_type).split('/')[0], "size": video.filesize_mb,
                            "quality": video.resolution, "item": str(video)
                        }
                        count = count + 1
                return render(request, "core/download.html", {'form': form, "audios": audios_dict, 
                                                              "videos": videos_dict, "title": title,
                                                              "thumbnail": thumbnail, "link": url_link})
        except Exception as e:
            messages.error(request, str(e))
            return redirect("show_available_download")

    return render(request=request, template_name="core/download.html", context={'form': form,
                                                                                "audios": audios_dict,
                                                                                "videos": videos_dict})

# def download(request):
#     if request.method == 'POST':
#         link = request.POST.get('link')
#         quality = request.POST.get('quality')
#         type = request.POST.get('type')
#     print(link, quality, type)
#     link = f"https://www.youtube.com/{link}"
#     download_path = os.path.join(Path.home(), 'Downloads')
#     videos = cache.get(f"{link}_videos")
#     if type == 'video' and videos:
#         video = [video for video in videos if video.resolution == quality]
#         stream = video[0]
#         return StreamingHttpResponse(stream)
#         response['Content-Disposition'] = f'attachment; filename="{stream.title}.mp4"'
#         return response
#         # response = HttpResponse(stream, content_type='video/mp4')
#         # response['Content-Disposition'] = f'attachment; filename="{stream.title}.mp4"'
#         # return response
#     return HttpResponse({})


def generate_large_file():
    for i in range(1, 1001):
        yield f"Line {i}\n"


def download(request):
    from pytube import YouTube
    yt=YouTube("https://www.youtube.com/watch?v=YLslsZuEaNE")
    audio=yt.streams.filter(only_audio=True)
    print(audio)
    response = StreamingHttpResponse(generate_large_file())
    response['Content-Disposition'] = f'attachment; filename="john.txt"'
    return response


def my_view(request, param1, param2):
    """
    A view that accepts two URL parameters and renders a template.

    Args:
        request: The HTTP request object.
        param1: The first URL parameter.
        param2: The second URL parameter.

    Returns:
        A rendered template with the parameters passed as context.
    """

    context = {
        'param1': param1,
        'param2': param2,
    }
    return render(request, 'core/my_template.html', context)
