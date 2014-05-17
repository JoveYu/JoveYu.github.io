<!--
.. title: POJ 1118 Lining Up C++版
.. slug: poj-1118
.. date: 2013-04-07T05:23:00+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1118](http://poj.org/problem?id=1118)


这个题要我们求出在2维坐标系内，共线的点的最大数值。

对于这样的题，最大的困难就是超时，这个也不利外，我的最先的思路是对于每两个点求k和b再对于一组k和b验证每一个，TLE！

后来优化了下，分别取i=0,j=i+1,m=j+1这样就很好的去除的重复的状况，另外验算的方法也改成了，比较三者斜率，一样则计数+1.

我第一次AC用了1625MS很大，后来试了改了下一段代码居然594MS，不过我觉得其实改了后应该是错的，因为我改的是，left和right的类型，本来是float改为int这样会由误差，但是可能OJ系统的数据比较好把，

代码如下：

	:::cpp
	/*Problem: 1118		User: awq123
	**Memory: 260K		Time: 594MS
	**Language: C++		Result: Accepted
	*/
	#include <cstdio>
	#include <iostream>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	struct point
	{
		int x,y;
	}p[700];

	int main()
	{
		int n,i,j,m,max,temp;
		while(cin>>n&&n;)
		{
			max=0;
			for(i=0;i<n;i++)
				scanf("%d%d",&p;[i].x,&p;[i].y);
			for(i=0;i<n;i++)	
				for(j=i+1;j<n;j++)
				{
					temp=0;
					for(m=j+1;m<n;m++)
					{
						int left=(p[i].x-p[m].x)*(p[j].y-p[m].y);
						int right=(p[j].x-p[m].x)*(p[i].y-p[m].y);
						if(left==right)
							temp++;
					}
					if(temp>max)
						max=temp;
				}	
			cout<<max+2<<endl;
		}
	}