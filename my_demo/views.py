from django.http import HttpResponse


def page_500(request):
    return HttpResponse("server is busy,please try again a later")