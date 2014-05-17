<!--
.. title: POJ 2248 Euclid's Game C++版
.. slug: poj-2248
.. date: 2013-04-07T05:42:00+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2248](http://poj.org/problem?id=2248)


一个博弈的题目，要求每次从多的里面拿少的倍数的棋子直到最后拿到0就算输。

一个关键的转折点a/b>1，谁碰到这个点就能赢，代码中排除几种特殊情况，既a＝b的情况，至于gcd函数就是求多少次会出现转折点！

代码如下：

	:::cpp
	/*Problem: 2348		User: awq123
	**Memory: 244K		Time: 32MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	using namespace std;

	int gcd(int n,int m)
	{
		int i=1;
		while(i++)
		{
			if(n<m)
				{int tmp=m;m=n;n=tmp;}  
			if(n/m>1)
				break;
			n-=m;
			if(m==0)
				break;
		}
		return i;
	}


	int main()
	{
		int a,b;
		while(cin>>a>>b&&a;&&b;)
		{
			if(a==b)
				cout<<"Stan wins"<<endl;
			else if(gcd(a,b)%2)
				cout<<"Ollie wins"<<endl;
			else
				cout<<"Stan wins"<<endl;
		}
	}

