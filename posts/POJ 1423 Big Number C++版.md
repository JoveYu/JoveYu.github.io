<!--
.. title: POJ 1423 Big Number C++版
.. slug: poj-1423
.. date: 2013-04-07T04:59:35+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1423](http://poj.org/problem?id=1423)

这个题就是求1<=m<=10^7的阶乘的位数

现开始自己用的老方法试了下，结果很容易想象，超时，搜索了网上的解体报告，对比了好多，找到了个最好的方法就是利用log函数巧妙的求位数，其中的原理还有点不明白，慢慢研究，数学不好的孩子伤不起啊！！

代码如下，很简洁：

	:::cpp
	/*Problem: 1423		User: awq123
	**Memory: 260K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cmath>
	#include <cstdio>
	using namespace std;

	int main()
	{
		int t,n;
		cin>>t;
		while(t--)
		{
			cin>>n;
		cout<<(int)(log10(sqrt(2*3.1415926*n))+n*(log10(1.*n)-log10(exp(1.))))+1<<endl;
		}

	}
