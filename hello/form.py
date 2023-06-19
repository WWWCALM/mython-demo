from django import forms


class FileForm(forms.Form):
    file = forms.FileField(
        # 支持多文件上传
        widget=forms.ClearableFileInput(),
        label='请选择文件',
    )
