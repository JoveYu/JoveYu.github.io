<!--
.. title: POJ 2249 Binomial Showdown C++版
.. slug: poj-2249-binomial-showdown-c
.. date: 2013-04-07T08:01:24+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1006](http://poj.org/problem?id=1006)


题目要求我们求组合数
公式如下



其中我们可以优化下算法，因为



这样k和n-k就取小的计算就是了，其中fixed指不使用科学计数法，其实用printf输出方便的多


代码如下：

	:::cpp
	/***************************************
	Problem: 2249		User: awq123
	Memory: 248K		Time: 0MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	#include <iomanip>
	using namespace std;

	int main()
	{
		double n,k,i,ans;
		while(cin>>n>>k&&n;+k)
		{
			ans=1;
			if(k>n-k)
				k=n-k;
			for(i=n;i>=n-k+1;i--)
				ans*=i;
			for(i=1;i<=k;i++)
				ans/=i;
			cout<<fixed<<setprecision(0)<<ans<<endl;
		}
	}
