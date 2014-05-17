<!--
.. title: POJ 2350 Above Average C++版
.. slug: poj-2350
.. date: 2013-04-07T05:58:32+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2350](http://poj.org/problem?id=2350)


水题，让我们求成绩高于平均成绩的百分比，然而这题没有给我们巨大的数据量，普通硬做就是了，不解释了！

代码如下：

	:::cpp
	/*Problem: 2350		User: awq123
	**Memory: 180K		Time: 16MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	using namespace std;

	int main()
	{
		int t,n,i,a[1000];
		float sum,num;
		scanf("%d",&t;);
		while(t--)
		{
			sum=0;
			num=0;
			scanf("%d",&n;);
			for(i=0;i<n;i++)
			{
				scanf("%d",&a;[i]);
				sum+=a[i];
			}
			sum/=n;
			for(i=0;i<n;i++)
				if(a[i]>sum)
					num++;
			printf("%2.3f%%n",100*num/n);
		
		
		}
	}