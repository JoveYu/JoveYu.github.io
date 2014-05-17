<!--
.. title: pre的那点事
.. slug: pre-overflow
.. date: 2013-05-07T13:11:59+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

想搞web什么都要学习，正在一点点修复博客的细节，今天就为一个小细节纠结了半天。

博客的代码高亮显示在pre标签中，这个是pygments自动生成的，也应该是个基本的标准吧。但是使用多了发现个问题，pre标签无法显示长度超过div标签长度的代码，虽然代码超过那个长度很少，而且规范的代码风格也不会允许你超过那个长度，但是少数语言种类，html，javascript多少都会很长的，考虑到这些我也开始尝试美化这个细节

##思路一，换行

这个思路就是让pre到长度不够的时候自动换行，这样后面遮住的代码就可以完整的显示出来了，网上找了相关的资料，主要的方法就是修改css，下面整理了一个比较全面的css方案：

```css
pre {
  white-space: pre-wrap;       /* css-3 */
  white-space: -moz-pre-wrap;  /* Mozilla, since 1999 */
  white-space: -pre-wrap;      /* Opera 4-6 */
  white-space: -o-pre-wrap;    /* Opera 7 */
  word-wrap: break-word;       /* Internet Explorer 5.5+ */
}
```

实测这个方案在chrome，firefox，ie8下是有效的，多余的我就不知道了！但是出来的结果让我不是很满意，首先，我的代码块没有设计行号，这个是为了美观，简洁，后面我们不打算加，那么换行后没有行号作为一个参考，就会显示的很乱，好吧，我放弃了！

##方案二，滚动条

换行不行就试试能不能在长度不够的时候自动添加滚动条，我觉得这个应该是个不错的解决方案，由于自己css记得不多，就只能找了，得到下面的方案

```css
pre {
  overflow: auto;
  overflow-y: hidden;
}
```

比较通俗不解释了，不过我有点疑问，为什么默认不设置overflow: auto呢，不过好歹问题解决了


最后的效果可以参考[这篇文章](http://jovesky.com/post/192/10django/)