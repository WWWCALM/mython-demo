import os

from django.http import HttpResponse, JsonResponse, FileResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import TemplateView

from hello.form import FileForm
from hello.models import FileModel


def hello_world(request):
    return HttpResponse('hello test')


def hello_china(request):
    return HttpResponse('hello china')


def get_parameter(request, month):
    return HttpResponse(month)


def get_list(request):
    """get """
    name = request.GET.get('name', '')
    print(name)
    return HttpResponse('get success')


def render_str(request):
    templ_name = 'index.html'
    html = render_to_string(template_name=templ_name)
    return HttpResponse(html)


def render_temp(request):
    return render(request, 'index.html')


def http_request(request):
    print(request.method)
    print(request.META)
    print(request.headers)
    print(request.headers['User-Agent'])
    print(request.GET.get('name', ''))
    return HttpResponse('response')


def http_response(request):
    resp = HttpResponse('resposenw', status=201)

    return resp;


def http_json(request):
    use_info = {
        'name': 'zhangsan',
        'age': 23

    }
    return JsonResponse(use_info)


def http_filr(request):
    responsefie = FileResponse(open('myfile.png', 'rb'))

    return responsefie


def no_data_404(request):
    return HttpResponse('404')


def parameter_404(request, id):
    if id < 1000:
        # return  HttpResponseRedirect('/hello/404')
        # return HttpResponseRedirect(reverse('no_data_404'))
        return redirect(no_data_404)
        # return redirect('www.baidu.com')
    return HttpResponse('内容', format(id))



def index_view(request):
    """
    上传文件
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            # 选择的文件
            files = request.FILES.getlist('file')

            # 遍历写入到数据库中
            for file in files:
                # 写入到数据库中
                file_model = FileModel(name=file.name, path=os.path.join('./upload', file.name))
                file_model.save()

                # 写入到服务器本地
                destination = open(os.path.join("./upload", file.name), 'wb+')
                for chunk in file.chunks():
                    destination.write(chunk)
                destination.close()

            # 提示上传成功
            return HttpResponse('上传成功!')
    else:
        form = FileForm()
        return render(request, 'upload.html', locals())



def download_view(request, id):
    """
    下载文件
    :param request:
    :param id:文件id
    :return:
    """
    file_result = FileModel.objects.filter(id=id)

    # 如果文件存在，就下载文件
    if file_result:

        file = list(file_result)[0]

        # 文件名称及路径
        name = file.name
        path = file.path

        # 读取文件
        file = open(path, 'rb')
        response = FileResponse(file)

        # 使用urlquote对文件名称进行编码
        response['Content-Disposition'] = 'attachment;filename="%s"' % urlquote(name)

        return response
    else:
        return HttpResponse('文件不存在!')


class HomeView(TemplateView):
       template_name = 'home.html'


def index_tpl(request):
    username = 'tom'
    age = 25
    img_url = '/media/dog.jpg'

    list_users = [
        {'name': 'zhangsan', 'age': 34},
        {'name': 'lisi', 'age': 35}
    ]
    return render(request,'home.html', {
        'username':username,
        'age': age,
        'img_url': img_url,
        'list_users': list_users
    })

