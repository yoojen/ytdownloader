from pytube import YouTube
from pytube.contrib.search import Search

def request_youtube_resource(yt_resource_link: str):
    """Module that send request to youtube api via pytube"""
    yt = YouTube(yt_resource_link)
    audios = yt.streams.filter(only_audio=True).order_by("abr")
    videos = yt.streams.filter(file_extension='mp4')

    return [audios, videos]


def search_youtube_resources(request, query: str):
    """Module that send search query request to youtube api via pytube"""
    yt = Search(query=query)
    if request.GET.get('next'):
        print("got ext")
        return yt.get_next_results()
    return yt

def requested_next_res(request):
    next_rs = search_youtube_resources()