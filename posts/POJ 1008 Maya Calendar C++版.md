<!--
.. title: POJ 1008 Maya Calendar C++版
.. slug: poj-1008
.. date: 2013-04-07T06:45:35+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1008](http://poj.org/problem?id=1008)


一个简单的历法转换，一种是365天20个月，一种是260天13个月，先计算出由第一天开始的天数，再进行转换，不难，注意月份的字符串就是了！


代码如下：

	:::cpp
	/***************************************
	Problem: 1008		User: awq123
	Memory: 168K		Time: 16MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		char hm[19][10]={
			"pop","no","zip","zotz","tzec","xul",
			"yoxkin","mol","chen","yax","zac",
			"ceh","mac","kankin","muan","pax",
			"koyab","cumhu","uayet"
		};
		char tm[20][10]={
			"imix","ik","akbal","kan","chicchan",
			"cimi","manik","lamat","muluk","ok",
			"chuen","eb","ben","ix","mem",
			"cib","caban","eznab","canac","ahau"
		};
		int i,t,n,y,d;
		char m[10];
		scanf("%d",&t;);
		printf("%dn",t);
		while(t--)
		{
			scanf("%d. %s %d",&d;,m,&y;);
			for(i=0;i<19;i++)
				if(strcmp(m,hm[i])==0)
					break;
			n=365*y+20*i+d;
			printf("%d %s %dn",n%260%13+1,tm[n%20],n/260);
		}
	}