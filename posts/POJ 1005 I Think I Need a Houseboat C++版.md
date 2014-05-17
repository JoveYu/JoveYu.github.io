<!--
.. title: POJ 1005 I Think I Need a Houseboat C++版
.. slug: poj-1005
.. date: 2013-04-07T06:01:36+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1005](http://poj.org/problem?id=1005)


水题，文字还一大串，题意就是那个半圆每年增加50平米，问多少年到(x，y)这个点

代码如下：

	:::cpp
	/*Problem: 1005		User: awq123
	**Memory: 252K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	using namespace std;
	int main()
	{
		float x,y;
		int t,n,i;
		cin>>n;
		for(i=1;i<=n;i++)
		{
			cin>>x>>y;
			t=3.1415926*(x*x+y*y)/2;
			cout<<"Property "<<i<<": This property will begin eroding in year "<<t/50+1<<"."<<endl;
		}
		cout<<"END OF OUTPUT."<<endl;
	}