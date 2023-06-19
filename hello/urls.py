from django.urls import path

from hello.views import hello_world, hello_china, get_parameter, get_list, render_str, render_temp, parameter_404, \
    no_data_404, index_view, download_view, HomeView, index_tpl

urlpatterns = [
    path('china/',hello_china,name='hello_world'),
    path('parameter/<int:month>',get_parameter),
    path('search',get_list),
    path('render/str',render_str),
    path('render/html',render_temp),
    path('404test/<int:id>',parameter_404),
    path('no_data_404',no_data_404),
    # 上传
    path('upload', index_view, name='index'),
    # 下载
    path('download/<id>', download_view, name='download'),
    path('homeclass',HomeView.as_view()),
    path('index_tpl',index_tpl)



]