<!--
.. title: POJ 3077 Rounders C++版
.. slug: poj-3077
.. date: 2013-04-07T08:52:43+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=3077](http://poj.org/problem?id=3077)


解释下题意，要求我们由个位开始在前面有一位的情况下进行四舍五入。

简单模拟四舍五入的运算，但是要注意就是第一位为9时会被动的多一位！废话不多说看代码

代码如下：

	:::cpp
	/*Problem: 3077		User: awq123
	**Memory: 1228K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		char d[1000000];
		int i,t;
		cin>>t;
		while(t--)
		{
			cin>>d;
			int len=strlen(d);
			if(len>1)
			{
				for(i=len-1;i>=1;i--)
				{
					if(d[i]>'4')
						d[i-1]++;
					d[i]='0';
				}
			}
			if(d[0]=='9'+1)
			{
				d[0]='0';
				cout<<'1';
			}
			cout<<d<<endl;
		}
	}