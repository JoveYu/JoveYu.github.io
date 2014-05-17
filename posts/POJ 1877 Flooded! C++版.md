<!--
.. title: POJ 1877 Flooded! C++版
.. slug: poj-1877
.. date: 2013-04-07T06:13:57+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1877](http://poj.org/problem?id=1877)

这个题是1999年的世界决赛，看似很简单，其实很难，对精度的要求很高！我一直WA到哭，没办法才找到原始数据比对，需要原始数据的可以留言我！


强烈推介下这个题！


解释下题意，有m*n的矩形地，每块100平米，提供每块地的高度，问给定一定的下雨量，水面的高度，及水面的覆盖率！

题目不难，只是因为这个是世界决赛，原始数据就有2500条！囧了！看到上面鲜红<span style="color: #ff0000;">Special Judge</span>

分析下思路，我们把高度排序，那么模型变为一个阶梯状的图形，可以补齐为矩形，然后利用每一个的底面积都是100，来计算，其中sum为已经计算过的了高度，d为每一个的高度，依次补齐诚矩形，当不够的时候，那么就是临界状况，然后利用v/100+d[i-1]计算出所有高度，再除以i得到水面高度！那么就是盖过了i块地，覆盖率就好求了！

代码如下：

	:::cpp
	/*Problem: 1877		User: awq123
	**Memory: 256K		Time: 47MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int d[900],sum[900];
		int m,n,i,j=1,v;
		while(cin>>m>>n&&m;&&n;)
		{
			for(i=0;i<m*n;i++)
				scanf("%d",&d;[i]);
			scanf("%d",&v;);
			sort(d,d+m*n);
			sum[0]=d[0];
			for(i=1;i<m*n;i++)
				sum[i]=d[i]+sum[i-1];
			for(i=1;i<m*n;i++)
			{
				if((d[i]*i-sum[i-1])*100>=v)
					break;
			}
			printf("Region %dn",j++);
			printf("Water level is %.2f meters.n",(v/100.0+sum[i-1])/i);
			printf("%.2f percent of the region is under water.nn",100.0*(float)i/(m*n));
		}
	}