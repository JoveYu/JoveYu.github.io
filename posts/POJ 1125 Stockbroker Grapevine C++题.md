<!--
.. title: POJ 1125 Stockbroker Grapevine C++题
.. slug: poj-1125
.. date: 2013-04-07T08:42:59+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1046](http://poj.org/problem?id=1046)


题意：股票经纪人要在一群人中散布一个传言，传言只能在认识的人中传递，题目将给出人与人的关系（是否认识），以及传言在某两个认识的人中传递所需的时间，要求程序给出以哪个人为起点，可以在好事最短的情况下，让所有人收到消息。

简化为有向连同图的最短路径问题，用floyd算法算法最简单，flyod算法的实现，我根据伪代码编写的：

	:::cpp
	void floyd()
	{
		for(int k=1;k<=n;k++)
			for(int i=1;i<=n;i++)
				for(int j=1;j<=n;j++)
					if(d[i][k]+d[k][j]<d[i][j])
						d[i][j]=d[i][k]+d[k][j];
		return;
	}

我也是第一次学习这个算法，给一个[传送门](http://zh.wikipedia.org/wiki/Floyd-Warshall%E7%AE%97%E6%B3%95)，其中算法实现很好理解，其中有介绍，DP思路也有写的比较详细。


代码如下：

	:::cpp
	/*Problem: 1125		User: awq123
	**Memory: 268K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	using namespace std;
	#define INF 0xFFFFF

	int n,d[105][105];

	void floyd()
	{
		for(int k=1;k<=n;k++)
			for(int i=1;i<=n;i++)
				for(int j=1;j<=n;j++)
					if(d[i][k]+d[k][j]<d[i][j])
						d[i][j]=d[i][k]+d[k][j];
		return;
	}

	int main()
	{
		int i,j,m;
		while(cin>>n&&n;)
		{
			for(i=1;i<=n;i++)
				for(j=1;j<=n;j++)
					if(i==j)
						d[i][j]=0;
						//相同初始化为0
					else
						d[i][j]=INF;
						//不同初始化为极大值
			for(i=1;i<=n;i++)//输入数据
			{
				cin>>m;
				for(j=1;j<=m;j++)
				{
					int p,c;
					cin>>p>>c;
					d[i][p]=c;
				}
			}
			floyd();//floyd算法
			int p,min=INF,max;
			for(i=1;i<=n;i++)
			{
				max=0;
				for(j=1;j<=n;j++)
					if(d[i][j]>max)
						max=d[i][j];
				if(max<min)
				{
					min=max;
					p=i;
				}
			}
			if(min==INF)
				cout<<"disjoint"<<endl;
			else
				cout<<p<<" "<<min<<endl;
		}
	}