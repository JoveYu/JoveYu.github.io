<!--
.. title: POJ 1338 Ugly Numbers C++版
.. slug: poj-1338
.. date: 2013-04-07T08:30:50+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1338](http://poj.org/problem?id=1338)


求第n个，因式只有2，3，5的树，打表做最好了，算法借鉴别人的，设d[]数组保存这个数列，这样，可以设三个指针p2，p3，p5，分别指向数列中的三个数（可以相同），取d[p2]*2，d[p3]*3，d[p5]*5中的最小者作为下一个数，并将该所对应的指标加1。不断重重该过程，直到求出第N个数为止。


代码如下：

	:::cpp
	/*Problem: 1338		User: awq123
	**Memory: 256K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	using namespace std;

	int main()
	{
		int d[1505];
		int p2=1,p3=1,p5=1,v2,v3,v5,i,n;
		d[1]=1;
		for(i=2;i<=1500;i++)
		{
			v2=d[p2]*2;
			v3=d[p3]*3;
			v5=d[p5]*5;
			if(v2<=v3&&v2;<=v5)
				d[i]=v2;
			if(v3<=v2&&v3;<=v5)
				d[i]=v3;
			if(v5<=v3&&v5;<=v2)
				d[i]=v5;
			if(d[i]==v2)
				p2++;
			if(d[i]==v3)
				p3++;
			if(d[i]==v5)
				p5++;
		}
		while(cin>>n&&n;)
		{
			cout<<d[n]<<endl;
		}
	}