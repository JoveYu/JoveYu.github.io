<!--
.. title: POJ 2215 Parliament C++版
.. slug: poj-2215
.. date: 2013-04-07T05:31:58+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2215](http://poj.org/problem?id=2215)


解释下题意，本题给出一个矩阵，然后每给出一个子矩阵的四个坐标，求子矩阵的和。

说下思路，每次输入数据的时候顺便做个简单的运算，来算出这个点到原点的所有的数的和，

在计算给定子矩阵的时候我们运用个简单的数学原理，如图



我们可以计算子矩阵的和，同面积的一种计算方法，利用r2s2-r1s2-r2s1+r1s1这样就行了，现开始错了几遍因为r1s1算的时候要减去1不然就没有算上上和左两条边！

这个题不敢用输入流，看到这种输入多的题，我就感觉要超时，虽然麻烦点，不过还是稳点把！！！

代码如下：

	:::cpp
	/*Problem: 2215		User: awq123
	**Memory: 4096K		Time: 63MS
	**Language: C++		Result: Accepted
	*/
	#include <cstdio>
	#include <iostream>
	#include <cstring>
	#include <algorithm>
	#include <cmath>
	using namespace std;

	int main()
	{
		int t,n,i,j,r,s,r1,r2,s1,s2,temp,a[1001][1001];
		scanf("%d",&n;);
		while(n--)
		{
			memset(a,0,sizeof(a));
			scanf("%d%d",&r;,&s;);
			for(i=1;i<=r;i++)
				for(j=1;j<=s;j++)
				{
					scanf("%d",&temp;);
					a[i][j]=temp+a[i][j-1]+a[i-1][j]-a[i-1][j-1];
				}
			scanf("%d",&t;);
			while(t--)
			{
				scanf("%d%d%d%d",&r1;,&s1;,&r2;,&s2;);
				r1--;s1--;
				temp=a[r2][s2]-a[r1][s2]-a[r2][s1]+a[r1][s1];
				printf("Absolutni hodnota pohodlnosti je %d bodu.n",temp);
			}
			printf("n");
		}
	}