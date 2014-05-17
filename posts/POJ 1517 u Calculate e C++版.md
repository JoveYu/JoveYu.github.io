<!--
.. title: POJ 1517 u Calculate e C++版
.. slug: poj-1517
.. date: 2013-04-07T07:52:40+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1517](http://poj.org/problem?id=1517)

根据公式计算输出就是了，不过这个公式是求e的，还找了下e的计算原理！

	:::cpp
	/***************************************
	Problem: 1517		User: awq123
	Memory: 168K		Time: 0MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		printf("n en- -----------n0 1n1 2n2 2.5n");
		double s=2.5,t=6;
		int a=3;
		while(a<10)
		{
			printf("%d %.9lfn",a,s=s+1/t);
			t*=++a;
		}
	}
