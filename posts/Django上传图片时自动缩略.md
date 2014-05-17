<!--
.. title: Django上传图片时自动缩略
.. slug: django-add-thumb
.. date: 2013-05-28T05:49:43+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

django中为大家提供便捷的图片上传功能，我的博客的图片类设计是这样的

```python
class Image(models.Model):
    UPLOAD_ROOT = '%Y/%m'
    title = models.CharField(max_length=100, unique=True,verbose_name=u'名称')
    image = models.ImageField(upload_to=UPLOAD_ROOT, verbose_name=u'图片')
```

挺简单的，但是这样传后，我也发现个问题，就是图片尺寸较大的，直接引用在页面中显示太大，而且速度也很慢，所以我想到生成缩略图，我的思路是再图片上传的时候进行缩略然后存储，有的人设计类的时候，设计原图和缩略同时存在的，原理也是类似，花了一个晚上，查了各种资料，还翻了下django源码，终于完成了。

首先看看怎么缩略图的生成，这里用的当然是PIL库了，缩略这样最基本的功能，实现起来不难，参考[这篇文章](http://imtx.me/archives/693.html)然后将处理完的图片传递给django保存即可，这里保存过程找了很多方法，查看源码后找出一种比较美观简洁的方法。

代码如下,这里把image重命名为PImage
```python
from django.db import models
from django.core.files.base import ContentFile
from PIL import Image as PImage
from cStringIO import StringIO

class Image(models.Model):
    UPLOAD_ROOT = '%Y/%m'
    title = models.CharField(max_length=100, unique=True, verbose_name=u'名称')
    image = models.ImageField(upload_to=UPLOAD_ROOT, verbose_name=u'图片')

    #自动缩略
    def save(self, *args, **kwargs):
        org_image = PImage.open(self.image)
        
        if org_image.mode not in ('L', 'RGB'):
            org_image = org_image.convert('RGB')
        
        size=580
        width, height = org_image.size
        if width > size:
            delta = width / size
            height = int(height / delta)
            org_image.thumbnail((size, height), PImage.ANTIALIAS)
        
        #获取文件格式   
        split = self.image.name.rsplit('.',1)
        format=split[1]
        if format.upper()=='JPG':
            format = 'JPEG'
            
        # 将图片存入内存
        temp_handle = StringIO()
        org_image.save(temp_handle, format)
        temp_handle.seek(0) # rewind the file
        
        # 保存图像
        self.image.save(self.image.name, ContentFile(temp_handle.getvalue()) , save=False)
        
        super(Image, self).save(*args, **kwargs)
```
具体效果是这样的![ubuntu][1]


  [1]: http://jovesky4django-uploads.stor.sinaapp.com/2013/05/Precise_Pangolin_by_Vlad_Gerasimov.jpg