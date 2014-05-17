<!--
.. title:  POJ 1316 Self Numbers C++版
.. slug: poj-1316
.. date: 2013-04-07T06:34:01+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1316](http://poj.org/problem?id=1316)


解释下题意，如果一个数可以写成另一个数及其个个位数的和，那么就不符合条件，比如39可以写成33+3+3那么不符合条件，要求输出所有符合条件的10000以内的数！

简单枚举，没什么算法，直接上代码：

	:::cpp
	/***************************************
	Problem: 1316		User: awq123
	Memory: 196K		Time: 0MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int a,b,c,d,n[10100]={0};
		for (int i = 1; i < 10000; i++)
		{
			if(n[i]==0)
				printf("%dn",i);
			a=i/1000;
			b=i%1000/100;
			c=i%100/10;
			d=i%10;
			n[i+a+b+c+d]=1;
		}

	}