<!--
.. title: POJ 2328 Guessing Game C++版
.. slug: poj-2328-guessing-game-c
.. date: 2013-04-07T08:02:51+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2328](http://poj.org/problem?id=2328)


解释下题意把，要求我们根据输入的猜测，来判断是否正确

我用l和r来表示区间的最小数和最大数，注意正确区间的更新，我的思路是
如果一个数too high但它小于l那么说谎，如果在l和r之间，更新r
如果一个数too low但它大于r那么说谎，如果在l和r之间，更新l
如果判断数时不在区间内，就是说谎。


代码如下：

	:::cpp
	/***************************************
	Problem: 2328		User: awq123
	Memory: 164K		Time: 16MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int l=0,r=11,n,flag=0;
		char ch[10];
		while(scanf("%d",&n;)&&n;)
		{
			getchar();
			scanf("%[^n]",ch);
			if(ch[4]=='t')
			{
				if(n<=l||n>=r)
					flag=1;
				if(flag)
					printf("Stan is dishonestn");
				else
					printf("Stan may be honestn");
				flag=0;
				l=0;
				r=11;
			}
			if(ch[4]=='h')
			{
				if(n<=l)
					flag=1;
				else
					if(n<r)
						r=n;
			}
			if(ch[4]=='l')
			{
				if(n>=r)
					flag=1;
				else
					if(n>l)
						l=n;
			}
		}
	}