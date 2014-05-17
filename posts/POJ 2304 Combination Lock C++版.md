<!--
.. title: POJ 2304 Combination Lock C++版
.. slug: poj-2304
.. date: 2013-04-07T08:02:53+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接： [http://poj.org/problem?id=2304](http://poj.org/problem?id=2304)


解释下题意，一个锁的表盘可以转动，共40格，输入abcd四个数，最开始表盘停在a上，先顺时针转两圈，然后顺时针转到b，再逆时针转一圈，在逆时针转到c，最后顺时针转到d，问一共转了多少度，注意是度不是上面的刻度，其中像0到30直接减会出现负数，我就加上个40然后取余数，就解决了

简单模拟，就是题意太难懂，


代码如下：

	:::cpp
	/***************************************
	Problem: 2304		User: awq123
	Memory: 248K		Time: 0MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int a,b,c,d,s;
		while(cin>>a>>b>>c>>d&&a;+b+c+d)
		{
			s=720;
			s+=(a-b+40)%40*360/40;
			s+=360;
			s+=(c-b+40)%40*360/40;
			s+=(c-d+40)%40*360/40;
			cout<<s<<endl;
		}
	}