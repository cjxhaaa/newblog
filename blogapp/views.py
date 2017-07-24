from django.http import Http404
from django.shortcuts import render, render_to_response,redirect,get_object_or_404
#reder必选参数：request，template_name
#render_to response必选参数template_name
from django.forms.models import modelformset_factory
from django.forms import Textarea,TextInput
from django.utils.translation import ugettext_lazy as _
from .forms import CommentForm
from .models import *


def get_blogs(request):
    #objects模型管理器
    #objects.all()返回包含数据库中所有对象的一个查询集
    #order_by()指定特定的排序
    blogs = Blog.objects.all().order_by('-pub_time')
    return render_to_response('blogapp/blog_list.html',{'blogs':blogs})

def get_details(request,blog_id):
    try:
        #objects.get(**kwargs)返回按照查询参数匹配到的对象
        #对于ForeignKey你可以使用字段名加上_id 后缀，id_exact等价于id等价于pk
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    CommentFormSet = modelformset_factory(
        Comment,fields=('name','context'),
        widgets={
            'name': TextInput(attrs={ 'placeholder': '输入昵称','rows': 1}),
            'context': Textarea(attrs={ 'placeholder': '说两句','rows': 4})},
        )
    if request.method == 'GET':
        form = CommentFormSet()
    else:
        form = CommentFormSet(request.POST)
        #is_valid()执行验证并返回一个表示数据是否合法的布尔值
        if form.is_valid():
            # #验证成功，表单数据将位于form.cleaned_data字典中
            cleaned_data = form.cleaned_data
            # # cleaned_data['blog'] = get_object_or_404(Blog,pk=blog_id)
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
            # form.save()
    ctx = {
        'blog': blog,
        'comments':blog.comment_set.all().order_by('-pub_time'),
        'form':form,
    }
    return render(request,'blogapp/blog_details.html',ctx)

# def comment(request,blog_id):
#     if request.method == 'GET':
#         form = CommentForm()
#     else:
#         form = CommentForm(request.POST)
#         #is_valid()执行验证并返回一个表示数据是否合法的布尔值
#         if form.is_valid():
#             #验证成功，表单数据将位于form.cleaned_data字典中
#             cleaned_data = form.cleaned_data
#             cleaned_data['blog'] = get_object_or_404(Blog,pk=blog_id)
#             Comment.objects.create(**cleaned_data)
#     ll = {
#         'comments':blog.comment_set.all().order_by('-pub_time'),
#         'form':form
#     }
#     return render(request,'blogapp/comment.html',ll)

