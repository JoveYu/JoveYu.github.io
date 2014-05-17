<!--
.. title: POJ 2301 Beat the Spread! C++版
.. slug: poj-2301-beat-spread-c
.. date: 2013-04-07T05:42:34+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2301](http://poj.org/problem?id=2301)


一早上起来，水一把！

a小于b或者ab奇偶性不同时输出impossible其他输出和的一半，差的一半

代码如下：

	:::cpp
	/*Problem: 2301		User: awq123
	**Memory: 252K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	using namespace std;

	int main()
	{
		int t,a,b,m,n;
		cin>>t;
		while(t--)
		{
			cin>>a>>b;
			m=(a+b)/2;
			n=(a-b)/2;
			if(a<b||(a+b)%2==1)
				cout<<"impossible"<<endl;
			else
				cout<<m<<" "<<n<<endl;
		}
	}