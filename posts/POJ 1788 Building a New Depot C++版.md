<!--
.. title: POJ 1788 Building a New Depot C++版
.. slug: poj-1788
.. date: 2013-04-07T05:03:00+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1788](http://poj.org/problem?id=1788)

这个题要求根据他给出的坐标组成的多边形求边长，不过这个幸好没有斜边，所有的都是横边与竖边，这样画出一个简单的坐标系，先求出全部的横边，再求出所有的竖边，利用qsort语句给结构体排序，先按x排求相邻两个相同的y的x差值加进s中，同理求出相邻两个相同的x的y差值，这样和就是总边长了。
其中两个比较的cmp函数写的很不错在这学习了！！

代码如下

	:::cpp
	/*Problem: 1788		User: awq123
	**Memory: 256K		Time: 16MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <algorithm>
	using namespace std;
	struct point
	{
		int x,y;
	}p[100001];

	int cmp1(const void *a,const void *b)
	{
		if(((point *)a)->x==((point *)b)->x)
			return ((point *)a)->y>((point*)b)->y ?1:-1;
		else
			return ((point *)a)->x>((point *)b)->x ?1:-1;
	}
	int cmp2(const void *a,const void *b)
	{
		if(((point *)a)->y==((point *)b)->y)
			return ((point *)a)->x>((point*)b)->x ?1:-1;
		else
			return ((point *)a)->y>((point *)b)->y ?1:-1;
	}

	int main()
	{
		int n,i,s;
		while(cin>>n&&n;)
		{
			for(i=0;i<n;i++)
				cin>>p[i].x>>p[i].y;
			s=0;
			qsort(p,n,sizeof(p[0]),cmp1);
			for(i=0;i<n-1;)
			{
				if(p[i].x==p[i+1].x)
				{
					s+=abs(p[i].y-p[i+1].y);
					i=i+2;
				}
				else
					i++;
			}
			qsort(p,n,sizeof(p[0]),cmp2);
			for(i=0;i<n-1;)
			{
				if(p[i].y==p[i+1].y)
				{
					s+=abs(p[i].x-p[i+1].x);
					i=i+2;
				}
				else
					i++;
			}
			cout<<"The length of the fence will be "<<s<<" units.n";
		}
	}