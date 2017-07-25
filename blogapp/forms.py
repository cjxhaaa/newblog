from django.forms import Form,ModelForm,Textarea,TextInput,CharField
from django.utils.translation import ugettext_lazy as _
from .models import Comment,Blog


# class CommentForm(ModelForm):
#     class Meta:
#         models = Comment
#         fields = ['name','context']
#         widgets = {
#             'name':TextInput(attrs={
#                 'placeholder':'输入昵称',
#                 'class': 'form-control'
#             }),
#             'context':Textarea(attrs={
#                 'placeholder':'说两句',
#                 'class': 'form-control',
#                 'rows':3
#             }),
#         }
#         labels = {
#             'name':_('昵称'),
#             'context':_('评论'),
#         }

class CommentForm(Form):
    name = CharField(label='昵称', max_length=16,
                     error_messages={
                         'required': '请填写您的称呼',
                         'max=length': '名称太长了'
                     },
                     widget=TextInput(attrs={
                         'class':'form-control',
                     })
                     )

    context = CharField(label='评论',
                        error_messages={
                            'required': '请填写您的评论！',
                            'max_length': '评论内容太长'
                        },
                        widget=Textarea(attrs={
                            'class':'form-control',
                            'rows':3
                        })
                        )