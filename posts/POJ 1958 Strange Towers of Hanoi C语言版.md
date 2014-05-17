<!--
.. title: POJ 1958 Strange Towers of Hanoi C语言版
.. slug: poj-1958
.. date: 2013-04-07T08:23:17+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1958](http://poj.org/problem?id=1958)


题目是一个变相的汉诺塔，问4个塔至少移动多少步！

先开始没看题以为就是普通汉诺塔，然后WA了半天才发现，本来汉诺塔我们可以套用公式，但4塔的我就没办法了！多塔问题，参考了[维基百科](http://zh.wikipedia.org/wiki/%E6%B1%89%E8%AF%BA%E5%A1%94)

其中这样描述的：
>令f(n,k)为在有k个柱子时，移动n个圆盘到另一柱子上需要的步数，则：
>对于任何移动方法，必定会先将m(1<=m<=n-1)个圆盘移动到一个中间柱子上，再将第n到第n-m个圆盘通过剩下的k-1个柱子移到目标柱子上，最后将m个在中间柱子上的圆盘移动到目标柱子上。这样所需的操作步数为2f(m,k) + f(n − m,k − 1)。

进行最优化，易得: ![1958](http://upload.wikimedia.org/math/7/9/8/79848829c8c4fdfdb1e542235a69488d.png)

这个递归公式适用于大于3的所有情况，但是我们只考虑4的情况，也就修改了下，具体见代码！


代码如下：

	:::cpp
	/*Problem: 1958		User: awq123
	**Memory: 172K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <cstdio>
	#include <cstring>
	#include <iostream>
	#include <algorithm>
	#include <cmath>
	using namespace std;

	int main()
	{
		int d[13];
		d[1]=1;
		d[2]=3;
		for(int i=3;i<=12;i++)
		{
			int min=999999;
			for(int j=1;j<i;j++)
			{
				if(min>2*d[j]+pow(2.0,(i-j))-1)
					min=2*d[j]+pow(2.0,(i-j))-1;
			}
			d[i]=min;
		}
		for(int i=1;i<=12;i++)
			printf("%dn",d[i]);
	}