<!--
.. title: POJ 2244 Eeny Meeny Moo C++版
.. slug: poj-2244
.. date: 2013-04-07T06:36:42+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2244](http://poj.org/problem?id=2244)


这个题简单约瑟夫问题，跟1012一个意思，不过比1012简单，方法一样，稍微调整一些细节就可以了。

题意是有n个城市，每隔m隔城市限电，1号第一个，问m为多少2号最后限电，我们可以这样看，就是n-1个城市从第一个开始数，保证第一个城市有电！

老样子利用公式：
	
	:::cpp
	p[i]=(p[i-1]+m-1)%(n-i);


约瑟夫，可以通用这个公式，不同的是我们要根据每个的实际情况稍微调整下！

代码如下：

	:::cpp
	/***************************************
	Problem: 2244		User: awq123
	Memory: 248K		Time: 16MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int n,m,i,p[155];
		while(cin>>n&&n;)
		{
			m=1;
			memset(p,0,sizeof(p));
			for(i=1;i<=n-2;i++)
			{
				p[i]=(p[i-1]+m-1)%(n-i);
				if(p[i]==0)
				{
					i=0;
					m++;
				}
			}
			cout<<m<<endl;
		}
	}