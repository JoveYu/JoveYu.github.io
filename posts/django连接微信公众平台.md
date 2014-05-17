<!--
.. title: django连接微信公众平台
.. slug: django-add-wechat
.. date: 2013-05-24T15:46:54+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

看到微信这么火，最近想尝试给自己的小站加个微信公众平台，不过结果估计也不会又多少人关注，纯当学习下django怎么调用别人的API把。

首先去微信公众平台的网站申请一个号，然后填写必要的信息，这么我就不罗列了，选择高级功能，打开开发者模式。然后会验证你的接口，这里我们再开始改造我们的django

###新建app
 
这里我们执行
```bash
python2 manage.py startapp wechat
```

###网站接入接口

微信公众平台验证接口，会发送GET请求到指定的URL，并带上四个参数，分别是signature微信加密签名，timestamp时间戳，nonce随机数，echostr随机字符串，通过检验signature来判断该请求是否来自微信服务器，这里会用到一个自己设参数token，相当与一个加密密钥，通过这个可以防止第三方伪造请求，如果判断成功就原样返回echostr那么就接入成功。

加密方式不复杂，文档里这样介绍的

>加密/校验流程：  
> 1. 将token、timestamp、nonce三个参数进行字典序排序  
> 2. 将三个参数字符串拼接成一个字符串进行sha1加密  
> 3. 开发者获得加密后的字符串可与signature对比，标识该请求来源于微信  

根据这个流程我们实现这样一个验证函数，通过python强大的标准库

```python
def checkSignature(request):
    signature=request.GET.get('signature',None)
    timestamp=request.GET.get('timestamp',None)
    nonce=request.GET.get('nonce',None)
    echostr=request.GET.get('echostr',None)
    #这里的token我放在setting，可以根据自己需求修改
    token=WECHAT_TOKEN

    tmplist=[token,timestamp,nonce]
    tmplist.sort()
    tmpstr="%s%s%s"%tuple(tmplist)
    tmpstr=hashlib.sha1(tmpstr).hexdigest()
    if tmpstr==signature:
        return echostr
    else:
        return None
```


###编写view

打开wechat中的views.py编写如下代码正确响应微信接入信号
```python
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import hashlib

@csrf_exempt
def index(request):
    if request.method=='GET':
        response=HttpResponse(checkSignature(request))
        return response
    else:
        return HttpResponse('Hello World')
```
python就是这样，语句永远跟自然语言相近，基本语义按顺序读下来就好

###配置url

我个人喜欢再app目录下单独管理每个app的url所以我再wechat目录下新建一个urls.py代码如下：
```python
from django.conf.urls import patterns, include, url

urlpatterns=patterns('',
    url(r'^$','wechat.views.index'),

)
```
然后在总urls里面添加
```python
urlpatterns += patterns('',
    url(r'^wechat/',include('wechat.urls')),
)
```

###最后启用app并验证

再setting中启用wechat，尝试下在公众平台中验证下，地址就是你自己配置的URL，token填写自己设的token，应该很快可以验证通过，这样你就拥有了微信公众平台的开发权限了

##一点想法

微信公众平台做的原来越好，看到很多优秀的微信应用，最近看36kr微信公众账号，感慨微信都支持自己添加菜单了，开放程度还是很高的，加上这种语音文字图像结合的交流方式，我感断言微信将会成为媲美微博的大平台，虽然现在自定义菜单还在内测相信要不了多久就能开放，下一步，准备简单添加几个功能，比如查看最新文章之类的！



