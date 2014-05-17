<!--
.. title: POJ 1328 Radar Installation c++版
.. slug: poj-1328
.. date: 2013-04-07T04:49:29+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1328](http://poj.org/problem?id=1328)

题意要求我们根据所给的坐标的点，选出最少得雷达安装数，若超出范围则为-1。

参考解题报告，应该利用贪心算法，先排出每个点的雷达安装范围，也就是结构体中的left和right，由左到右摆放雷达，用std表示雷达的最远安装范围，在范围不够的时候加设一台，然后更新雷达覆盖范围，这样就能够求出雷达的最小值，其中的细节还需好好研究下，更新标准点的算法是重点！
代码如下：

	:::cpp
	#include <iostream>
	#include <cmath>

	typedef struct
	{
		double left;
		double right;
	}point;

	point p[1001];
	int n, d, sum;

	void Solve()
	{
		int i;
		sum = 1;
		point temp;
		double std;
		//对岛坐标进行排序
		for (int m=0;m<n;m++)
			for(int j=m+1;j<n;j++)
				if (p[m].left>p[j].left)
				{
					temp=p[m];
					p[m]=p[j];
					p[j]=temp;
				}
		std = p[0].right;
		//第一个点的右坐标作为起始参考
		for (i = 1; i < n; i++)
		{
			if (p[i].left > std)
			{
				std = p[i].right;
				//更新参考
				sum++;
			}
			else
			{
				//某点右坐标比标准值小，更新标准值为该点右坐标
				if (p[i].right < std)
				{
					std = p[i].right;
				}
			}
		}
	}

	int main()
	{
		int x, y, i, t, fail;
		t = 1;
		while(1)
		{
			fail = 0;
			scanf("%d%d", &n;, &d;);
			if(n + d == 0) break;
			for (i = 0; i < n; i++)
			{
				scanf("%d%d", &x;, &y;);
				if (y > d)
					fail = 1;
				else
				{
					//求出这个点最远的雷达点
					p[i].left = x - sqrt((double)(d * d - y * y));
					p[i].right = x + sqrt((double)(d * d - y * y));
				}
			}
			if (fail)
			{
				printf("Case %d: -1n", t++);
			}
			else
			{
				Solve();
				printf("Case %d: %dn", t++, sum);
			}
		}
	}
