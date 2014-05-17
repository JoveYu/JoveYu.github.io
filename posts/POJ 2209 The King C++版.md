<!--
.. title: POJ 2209 The King C++版
.. slug: poj-2209
.. date: 2013-04-07T06:36:17+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2209](http://poj.org/problem?id=2209)


水题，就是求n个数的e次幂，如何加最大！必然是不加负数就是了！


代码如下：

	:::cpp
	/***************************************
	Problem: 2209		User: awq123
	Memory: 252K		Time: 16MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int i,n,e,son[101],sum=0;
		cin>>n>>e;
		for(i=1;i<=n;i++)
		{
			cin>>son[i];
			if(e==1&&son;[i]>0)
				sum+=son[i];
			if(e==2)
				sum+=son[i]*son[i];
			if(e==3&&son;[i]>0)
				sum+=son[i]*son[i]*son[i];
		}
		cout<<sum<<endl;
	}