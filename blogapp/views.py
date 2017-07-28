from django.shortcuts import render, render_to_response,redirect,get_object_or_404
#reder必选参数：request，template_name
#render_to response必选参数template_name
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.mail import send_mail
from .forms import CommentForm
from .models import *
import re


# def get_blogs(request):
#     #objects模型管理器
#     #objects.all()返回包含数据库中所有对象的一个查询集
#     #order_by()指定特定的排序
#     blogs = Blog.objects.all().order_by('-pub_time')
#     return render_to_response('blogapp/blog_list.html',{'blogs':blogs})

class IndexView(ListView):
    model = Blog
    template_name = 'blogapp/blog_list.html'
    context_object_name = 'blog_list'
    #添加额外的内容
    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        #添加以上变量到上下文中，同时返回默认上下文的变量
        return super(IndexView,self).get_context_data(**kwargs)

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogapp/blog_details.html'
    context_object_name = 'blog'
    #pk_url_kwarg接收来自url中的逐渐，然后根据逐渐进行查询
    pk_url_kwarg = 'blog_id'
    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['form'] = CommentForm()
        kwargs['comments'] = self.object.comment_set.all()
        return super(BlogDetailView,self).get_context_data(**kwargs)

class CategoryView(ListView):
    model = Blog
    template_name = 'blogapp/blog_list.html'
    context_object_name = 'blog_list'
    #get_querysett()获取Model列表，同时加入了自己的逻辑
    def get_context_data(self, **kwargs):
        kwargs['blog_list'] = Blog.objects.filter(category=self.kwargs['cate_id'])
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['category_name'] = get_object_or_404(Category,pk=self.kwargs['cate_id'])
        return super(CategoryView, self).get_context_data(**kwargs)

class ArchivesView(ListView):
    model = Blog
    template_name = 'blogapp/archives.html'
    context_object_name =  'blog_list'
    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['blogyear_list'] = BlogYear.objects.all().order_by('-name')
        return super(ArchivesView,self).get_context_data(**kwargs)

def CommentView(request,blog_id):
    if request.method == 'POST':
        #获取POST表单数据
        form = CommentForm(request.POST)
        #is_valid()执行验证并返回一个表示数据是否合法的布尔值
        if form.is_valid():
            # #验证成功，表单数据将位于form.cleaned_data字典中
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = get_object_or_404(Blog,id=blog_id)
            #create在一步操作中同时创建并保存
            Comment.objects.create(**cleaned_data)
            return redirect('blog:blog_get_detail',blog_id=blog_id)

def SuggestView(request):
    if request.method == 'POST':

        send_mail(
            '访客建议',
            request.POST['message'],
            '405019079@qq.com',
            ['405019079@qq.com']
        )
        return redirect('blog:thanks')

def Thanks(request, ):
    return render(request, 'blogapp/thanks.html')


# def get_details(request,blog_id):
#     try:
#         #objects.get(**kwargs)返回按照查询参数匹配到的对象
#         #对于ForeignKey你可以使用字段名加上_id 后缀，id_exact等价于id等价于pk
#         blog = Blog.objects.get(id=blog_id)
#     except Blog.DoesNotExist:
#         raise Http404
#     if request.method == 'POST':
#         #获取POST表单数据
#         form = CommentForm(request.POST)
#         #is_valid()执行验证并返回一个表示数据是否合法的布尔值
#         if form.is_valid():
#             # #验证成功，表单数据将位于form.cleaned_data字典中
#             cleaned_data = form.cleaned_data
#             cleaned_data['blog'] = blog
#             Comment.objects.create(**cleaned_data)
#     else:
#         form = CommentForm()
#     ctx = {
#         'blog': blog,
#         'comments':blog.comment_set.all().order_by('-pub_time'),
#         'form':form,
#     }
#     return render(request,'blogapp/blog_details.html',ctx)
