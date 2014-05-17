<!--
.. title: django智能分页函数
.. slug: django-pagination-11
.. date: 2013-09-14T14:44:24+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

django中提供便捷的分页服务，主要通过
Pagination来实现的，详细可以参考[Django文档][1]，通过简单设立每页显示的数量，来自动化获得分页object_list，先来看看调用方式，借用文档里面的例子：

```python
>>> from django.core.paginator import Paginator
>>> objects = ['john', 'paul', 'george', 'ringo']
>>> p = Paginator(objects, 2)#新建分页，参数为所有的obj，和每页显示数量
>>> p.count#所有的obj的数量
4
>>> p.num_pages#分出来的页数
2
>>> p.page_range#页数的列表
[1, 2]
>>> page1 = p.page(1)#得到第一页
>>> page1
<Page 1 of 2>
>>> page1.object_list#第一页的obj列表
['john', 'paul']

>>> page2 = p.page(2)
>>> page2.object_list
['george', 'ringo']
>>> page2.has_next()#是否有下一页
False
>>> page2.has_previous()#是否有前一页
True
>>> page2.has_other_pages()#是否有其他页
True
>>> page2.next_page_number()#下一页的地址，这里最好判断是否有，不然会异常
Traceback (most recent call last):
...
EmptyPage: That page contains no results
```

其实分页并不是一个复杂的流程，但是我跟喜欢使用官方提供的功能，省的自己浪费没有必要的时间，但是在使用的过程中，还是优点满足不了我们的用途，一般写导航的时候都会显示当前页前后3-4也的导航，向这样的：

![导航][2]

而我们仅仅能得到一个所有的列表，加之每次都要在模板里配置嫌多判断，前不久学习了一种好的写法，稍微改造了下，封装了下，代码如下：
```python
def my_pagination(request, queryset, display_amount=15, after_range_num = 5,bevor_range_num = 4):
    #按参数分页
    paginator = Paginator(queryset, display_amount)
    try:
        #得到request中的page参数
        page =int(request.GET.get('page'))
    except:
        #默认为1
        page = 1
    try:
        #尝试获得分页列表
        objects = paginator.page(page)
    #如果页数不存在
    except EmptyPage:
        #获得最后一页
        objects = paginator.page(paginator.num_pages)
    #如果不是一个整数
    except:
        #获得第一页
        objects = paginator.page(1)
    #根据参数配置导航显示范围
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+bevor_range_num]
    else:
        page_range = paginator.page_range[0:page+bevor_range_num]
    return objects,page_range
```
在模板中配套加入代码，这个模板使用bootstrap应该很好理解

分页出来的数据处理，像这样写
```htmldjango
{% if objects.object_list %}
    {% for p in objects.object_list %}
    ...
    {% endfor %}
{% else %}
...
{% endif %}
```

然后在下面加入导航
```htmldjango
<div class="pagination pagination-centered">
  <ul>
    {% if objects.has_previous %}
    <li><a href="?page={{ objects.previous_page_number }}">前一页</a></li>
    {% else %}
    <li class="active"><a>前一页</a></li>
    {% endif %}

    {% for p in page_range %}
      {% ifequal p objects.number %}
      <li class="active"><a>{{p}}</a></li>
      {% else %}
      <li><a href="?page={{p}}" title="第{{p}}页">{{p}}</a><li>
      {% endifequal %}
    {% endfor %}

    {% if objects.has_next %}
    <li><a href="?page={{ objects.next_page_number }}">后一页</a></li>
    {% else %}
    <li class="active"> <a>后一页</a></li>
    {% endif %}
  </ul>
</div>
```
大家可能还关心view怎么写，给一个简单的示例吧：
```python
def my_view(request):
    all_objects = some_model.objects.all()
    objects, page_range = my_pagination(request, all_objects)
    return render_to_response('a_template.html',{'objects':objects,'page_range':page_range},context_instance=RequestContext(request))
```

简单来说下这样写的好处，一方面不用关心处理的逻辑，一方面不需要对模板进行特殊处理，将request传进去，连page参数都不用操心，相信这样的一个分页函数能帮到你！

  [1]: https://docs.djangoproject.com/en/1.5/topics/pagination/
  [2]: http://jovesky4django-uploads.stor.sinaapp.com/2013/09/pagination.png "pagination"