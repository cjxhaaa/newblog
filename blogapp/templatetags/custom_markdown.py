import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)  # 注册template filter
@stringfilter  # 希望字符串作为参数
def custom_markdown(value):
    return mark_safe(markdown.markdown(value,
                                       extensions=['markdown.extensions.fenced_code', # 解析代码块
                                                   'markdown.extensions.codehilite',   # 为代码高亮准备
                                                   'markdown.extensions.extra',
                                                   ],
                                       safe_mode=False,
                                       enable_attributes=False))
