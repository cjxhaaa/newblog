from django import template
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

#模板库支持
register = template.Library()
# 这个装饰器表明这个函数是一个模板标签，takes_context = True 表示接收上下文对象，就是前面所说的封装了各种变量的Context对象。
@register.simple_tag(takes_context=True)
def paginate(context,object_list,page_count):
    left = 3
    right = 3
    # 实例化结果，每页page_count条数据，少于2条合并到上一页
    paginator = Paginator(object_list,page_count,2)
    # 接收网页中page值
    page = context['request'].GET.get('page')
    try:
        # 传入html当前页对象
        object_list = paginator.page(page)
        context['current_page'] = int(page)
        pages = get_left(context['current_page'],left,paginator.num_pages) + get_right(context['current_page'],left,paginator.num_pages)
    # 异常处理，如果用户传递的page值不是整数，则把第一页的值返回给他
    except PageNotAnInteger:
        object_list = paginator.page(1)
        context['current_page'] = 1
        pages = get_right(context['current_page'], left,paginator.num_pages)
    # 如果用户传递的 page 值是一个空值，那么把最后一页的值返回
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
        context['current_page'] = paginator.num_pages
        pages = get_left(context['current_page'], left, paginator.num_pages)

    context['blog_list'] = object_list
    context['pages'] = pages
    context['last_page'] = paginator.num_pages
    context['first_page'] = 1
    try:
        context['pages_first'] = pages[0]
        context['pages_last'] = pages[-1] + 1

    except IndexError:
        context['pages_first'] = 1
        context['pages_last'] = 2
    return ''

def get_left(current_page,left,num_pages):
    '''
    辅助函数，获取当前页码值的左边两个页码值
    '''
    if current_page == 1:
        return []
    elif current_page == num_pages:
        l = [i - 1 for i in range(current_page, current_page - left, -1) if i - 1 > 1]
        l.sort()
        return l
    l = [i for i in range(current_page, current_page - left, -1) if i > 1]
    l.sort()
    return l

def get_right(current_page,right,num_pages):
    '''
    辅助函数，获取当前页码右边两个页码值 
    '''
    if current_page == num_pages:
        return []
    return [i + 1 for i in range(current_page, current_page +right - 1) if i < num_pages - 1]

