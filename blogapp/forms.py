from django.forms import Form,ModelForm,Textarea,TextInput,CharField
from django.utils.translation import ugettext_lazy as _
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        models = Comment
        fields = ['name','context']
        widgets = {
            'name':TextInput(attrs={
                'placeholder':'输入昵称',
            }),
            'context':Textarea(attrs={
                'placeholder':'说两句',
                'rows':4
            })
        }
        labels = {
            'name':_('昵称'),
            'context':_('评论'),
        }

# class CommentForm(Form):
#     name = CharField(label='昵称', max_length=16, error_messages={
#         'required': '请填写您的称呼',
#         'max=length': '名称太长了'
#     })
#
#     context = CharField(label='评论内容', error_messages={
#         'required': '请填写您的评论！',
#         'max_length': '评论内容太长'
#     })
