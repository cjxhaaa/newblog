from django import forms


class CommentForm(forms.Form):
    '''
    评论表单用于发表博客评论。表单的类根据需求定义三个字段：称呼、邮箱、评论
    '''
    name = forms.CharField(label='称呼', max_length=16, error_messages={
        'required': '请填写您的称呼',
        'max=length': '名称太长了'
    })

    email = forms.EmailField(label='邮箱', error_messages={
        'required': '请填写您的邮箱',
        'invalid': '邮箱格式不正确'
    })

    context = forms.CharField(label='评论内容', error_messages={
        'required': '请填写您的评论！',
        'max_length': '评论内容太长'
    })
