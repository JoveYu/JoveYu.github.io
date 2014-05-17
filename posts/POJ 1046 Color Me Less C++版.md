<!--
.. title: POJ 1046 Color Me Less C++版
.. slug: poj-1046
.. date: 2013-04-07T06:28:20+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：<[http://poj.org/problem?id=1046](http://poj.org/problem?id=1046)


水题，解释下题意，其中讲到了RGB颜色，给了个公式：

![1046](http://poj.org/images/1046/color.gif)

其中D越小说明，颜色越接近，输入16个点，在后面每组数据求最接近的颜色，也就是最近的坐标点。

暴力枚举就是了，没什么好解释的，还有其实不用开根号的！

	:::cpp
	/***************************************
	Problem: 1046		User: awq123
	Memory: 136K		Time: 0MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int i,d[16][3],r,g,b;
		for (i = 0; i < 16; i++)
			scanf("%d%d%d",&d;[i][0],&d;[i][1],&d;[i][2]);
		while(scanf("%d%d%d",&r;,&g;,&b;)==3&&!(r==-1&&g;==-1&&b;==-1))
		{
			int min=100000,len,n;
			for (i = 0; i < 16; i++)
			{
				len=(r-d[i][0])*(r-d[i][0])+(g-d[i][1])*(g-d[i][1])+(b-d[i][2])*(b-d[i][2]);
				if (len<min)
				{
					min=len;
					n=i;
				}
			}
			printf("(%d,%d,%d) maps to (%d,%d,%d)n",r,g,b,d[n][0],d[n][1],d[n][2]);
		}
	}