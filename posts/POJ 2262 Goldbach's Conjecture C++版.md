<!--
.. title: POJ 2262 Goldbach's Conjecture C++版
.. slug: poj-2262
.. date: 2013-04-07T05:41:30+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2262](http://poj.org/problem?id=2262)


这个题很熟悉书上就有，输出一个数写成两个素数的和的形式；

看到题的时候就可以想到，如果针对每一次输入去判断素数会很费时间，那么我们先用一个数组去判断素数，再统一运算。

讲下我的算法，由小到大，依次判断，如果这个数为素数，那么它和任意数的乘积都不是素数，依次推出所有的情况。

后面的不说了，没什么好说的！

对了，为什么我没有判断，不存在的情况也能过？不是应该加个else吗？这是因为，no else，每一个数都能写成两个素数的形式，这是哪个老家伙说的啊？不是很记得了！

代码如下：

	:::cpp
	/*Problem: 2262		User: awq123
	**Memory: 4172K		Time: 485MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	using namespace std;

	int main()
	{
		int n[1000000],i,j,t;
		memset(n,0,sizeof(n));//0是1不是
		for(i=2;i<1000000;i++)
			if(n[i]==0)
				for(j=2;i*j<1000000;j++)
					n[i*j]=1;
		while(cin>>t&&t;)
		{
			for(i=3;i<=t/2;i+=2)
				if(n[i]==0&&n;[t-i]==0)
				{
					cout<<t<<" = "<<i<<" + "<<t-i<<endl;
					break;
				}
		}
	}