<!--
.. title: JSON与JSONP分析，含调用实例
.. slug: json-jsonp
.. date: 2013-09-28T08:04:47+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

AJAX是目前web开发少不了的环节，在很多时候不仅仅是get或者post数据，更重要的是要得到返回的数据，在我所开发的项目中大部分推崇的都是使用json作为返回格式，不仅在webapi上调用方便，在客户端上也有各种解析库！

作为一个web新手，逐渐使用AJAX频繁，也就自然而然的遇到了AJAX的跨域问题，这个时候我遇到了jsonp，仅仅多了一个字，不难看出他的本质还是json，但是他能够完成我们头疼的跨域问题

这篇文章就是用来解释这样一个问题，json和jsonp有什么区别，jsonp怎么调用，如果你是个web老手完全可以去冲咖啡了，刚刚学习，以此为记！没有什么人指点，可能很多都是我的个人见解。

<!-- TEASER_END -->

# 关于JSONP

jsonp是开发人员，利用script标签的特性，巧妙的解决跨域AJAX请求，而开发出来的一个第三方标准，因为script的src属性是没有限制的，利用其加载接口，得到一段代码，格式上是一个函数调用，而把我们需要的json巧妙的作为参数。

参考：[http://zh.wikipedia.org/wiki/JSONP][1]

# JSONP使用条件

比如我们平常写接口使用的返回，一般会是这样，一段简单的JSON：

```javascript
{"ret":true ,"msg":"" }
```

如果是JSONP的返回会是这样：

```javascript
callback({"ret":true, "msg":""})
```

区别显而易见，jsonp相当于就是在json外面用一个回调函数包起来，我们如果把jsonp堪称一段javascript的话，把括号中间的看做一个实体，你会发现这个就是在调用callback函数，然后把中间的作为参数传递进去。分析到这我们来总结下jsonp的使用条件：

 1. 接口返回能使用回调函数将返回json包裹
 2. 调用页面拥有一个函数，名字与那个回调函数相同，并拥有处理数据的能力
 3. 调用页面能运行这段javascript

# JSONP的调用

这里我没有合适的接口演示，找了个寻找电话归属地的接口做演示，接口地址为`https://www.baifubao.com/callback?cmd=1059&callback=phone&phone=13909161860`
注意这个接口其中的callback参数，这个就是接口会附带的回调函数名，打开就可以看到那个phone了！

使用javascript调用的，原理就是在网页中添加一个script标签，然后src地址指向这个接口，然后浏览器会运行这个地址里的javascript，然后调用这个函数：

```html
<script type="text/javascript">
    // 构建回调函数处理返回数据
	var phone = function(data){
        alert('你查询的归属地:'+data.data.area_operator);
    };
    var url = "https://www.baifubao.com/callback?cmd=1059&callback=phone&phone=13909161860";
    // 创建script标签，设置其属性
    var script = document.createElement('script');
    script.setAttribute('src', url);
    // 把script标签加入head，此时调用开始
    document.getElementsByTagName('head')[0].appendChild(script); 
</script>
```

查看演示：

<script type="text/javascript">
// 构建回调函数处理返回数据
function phone(data){
    alert('你查询的归属地:'+data.data.area_operator);
};
function runjsonp(){
    var url = "https://www.baifubao.com/callback?cmd=1059&callback=phone&phone=13909161860";
    // 创建script标签，设置其属性
    var script = document.createElement('script');
    script.setAttribute('src', url);
    // 把script标签加入head，此时调用开始
    document.getElementsByTagName('head')[0].appendChild(script); 
}
</script>
<input type="button" value="点我点我点我" onclick="runjsonp()">

这样的调用方法是最基本的，现在所有支持jsonp的框架，无论是jquery还是extjs，他们实现jsonp的方法的根本也是大同小异，在我们实际生产环境中，利用框架绝对是首选，下面在演示两种jquery的调用方法：

### 使用$.getJSON()

使用两个参数，一个是请求地址，一个是回调函数

代码如下：

```html
<script type="text/javascript">
	$.getJSON("https://www.baifubao.com/callback?cmd=1059&callback=?&phone=13909161860",function(data){
		alert('你查询的归属地:'+data.data.area_operator);
	});
</script>
```

这里就有一个疑问了，我的回调函数了，显示是个'?'这个是什么？是一个函数名？明显不是，这个可以理解为jquery用来代替它自动生成的函数名的标记，只要用?代替回调函数名就可以成功调用jsonp了


### 使用$.ajax()

参数和一般调用一样

```html
<script type="text/javascript">
	$.ajax({
		type:"get",
		url:"https://www.baifubao.com/callback?cmd=1059&phone=13909161860",
		dataType:"jsonp",
		jsonp:"callback",
		//jsonpCallback:"phone",可以指定回调的函数名
		success:function(data){
			alert('你查询的归属地:'+data.data.area_operator);
		}
	});
</script>
```

# 总结

学习完jsonp不得不佩服，我大程序猿的智慧，利用一个小技巧成功解决跨域问题，并且还衍生出一套web标准，javascript的学习还没有结束，像这样的小技巧还等着我发现！


  [1]: http://zh.wikipedia.org/wiki/JSONP
