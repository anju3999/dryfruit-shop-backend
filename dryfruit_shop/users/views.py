from django.http import HttpResponse

def user_list(request):
    return HttpResponse('user_list here')

def user_detail(request):
    return HttpResponse('user_detail here')

def user_edit(request):
    return HttpResponse('user_edit here')