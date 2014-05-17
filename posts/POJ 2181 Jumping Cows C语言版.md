<!--
.. title: POJ 2181 Jumping Cows C语言版
.. slug: poj-2181
.. date: 2013-04-07T08:26:49+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2181](http://poj.org/problem?id=2181)


题目给你一些数，让你找出一个子序列，子序列计算的规则是：奇数位相加偶数位相减。要求这个子序列计算的值最大为多少！

也就是总数+奇数位-偶数位的子串；

先开始没什么思路，查阅了下解体报告，发现，我们只要找比相邻都高的数为奇数位，比相邻都底的数做偶数位就可能得到最大的值！


代码如下

	:::cpp
	/*Problem: 2181		User: awq123
	**Memory: 752K		Time: 63MS
	**Language: C++		Result: Accepted
	*/
	#include <cstdio>
	#include <cstring>
	#include <iostream>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int i,n,d[150005];
		scanf("%d",&n;);
		for(i=1;i<=n;i++)
			scanf("%d",&d;[i]);
		int flag=1,sum=0;
		for(i=1;i<=n;i++)
			if(flag)
			{
				if(d[i]>=d[i+1]&&d;[i]>=d[i-1])
				{
					sum+=d[i];
					flag=0;
				}
			}
			else
			{
				if(d[i]<=d[i+1]&&d;[i]<=d[i-1])
				{
					sum-=d[i];
					flag=1;
				}
			}
		printf("%dn",sum);
	}