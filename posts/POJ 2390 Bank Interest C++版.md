<!--
.. title: POJ 2390 Bank Interest C++版
.. slug: poj-2390
.. date: 2013-04-07T08:08:02+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2390](http://poj.org/problem?id=2390)


水题，要我们求给出本金m，y年后按，r计算后的本息和。注意数据大小！


代码如下：

	:::cpp
	/***************************************
	Problem: 2390		User: awq123
	Memory: 180K		Time: 16MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		double r,m,y;
		scanf("%lf%lf%lf",&r;,&m;,&y;);
		for(int i=0;i<y;i++)
			m*=(100+r)/100;
		printf("%.0lf",m-0.5);
	}
