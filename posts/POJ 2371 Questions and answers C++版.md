<!--
.. title: POJ 2371 Questions and answers C++版
.. slug: poj-2371
.. date: 2013-04-07T05:08:46+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2371](http://poj.org/problem?id=2371)


水题 没什么好解释的，题意要求先输入一个数N在输入N个数，以###分开，排序后，输入数N，再输入N个数，每输入一个数，求这个数位置上的数，本来题意很简单的，不理解为什么写这么复杂。

一大早起来作个题娱乐下，无提升。

代码如下：

	:::cpp
	/*Problem: 2371		User: awq123
	**Memory: 608K		Time: 63MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	#include <vector>
	using namespace std;

	int main()
	{
		int m,n,i;
		char s[3];
		vector<int> num(100000);
		scanf("%d",&m;);
		for(i=0;i<m;i++)
			scanf("%d",&num;[i]);
		sort(num.begin(),num.begin()+m);
		cin>>s;
		scanf("%d",&n;);
		while(n--)
		{
			scanf("%d",&i;);
			printf("%dn",num[i-1]);
		}
	
	}
