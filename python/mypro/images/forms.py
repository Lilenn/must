from urllib import request
from django.core.files.base import ContentFile
from uuslug import slugify
from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title','url','description')

    def clean_url(self):
        url = self.cleaned_data['url']
        vaild_extensions = ['jpg','jpeg','png']
        extension = url.rsplit('.',1)[1].lower()
        if extension not in vaild_extensions:
            raise forms.ValidationError('您所提供的图片地址格式不支持')
        return url

    def save(self, commit=True):
        image = super(ImageCreateForm,self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{}.{}'.format(slugify(image.title),image_url.rsplit('.',1)[1].lower())
        #根据url下载图片
        response = request.urlopen(image_url)
        image.image.save(image_name,ContentFile(response.read()),save=False)

        if commit:
            image.save()
        return image

