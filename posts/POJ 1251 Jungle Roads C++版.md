<!--
.. title: POJ 1251 Jungle Roads C++版
.. slug: poj-1251
.. date: 2013-04-07T08:37:18+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1251](http://poj.org/problem?id=1251)


第一个自己做的最小生成树的题，利用的prim算法，虽然其中编写时调试还是参考了一些文章，不过对prim算法有了一些了解

题意，就是求给出数据的最小生成树。

prim简单的来说就是每次加上与已选择点相连的最短线。利用了贪心的思路。具体见注释！


代码如下：

	:::cpp
	/*Problem: 1251		User: awq123
	**Memory: 264K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	using namespace std;
	#define INF 0x7FFFFF

	int n,map[30][30];

	int min(int a,int b)
	{
		return a>b?b:a;
	}

	void prim()
	{
		int i,mark[30],lcos[30];//mark标记是否被选择
		memset(mark,0,sizeof(mark));
		for(i=1;i<=n;i++)//初始话lcos为极大
			lcos[i]=INF;
		lcos[1]=0;
		while(1)
		{
			int mins=INF,v=-1;
			for(i=1;i<=n;i++)//寻找最短的相连线段
				if(mark[i]==0&&lcos;[i]<mins)
				{
					mins=lcos[i];
					v=i;
					//记录这个点
				}
			if(v==-1)//如果没有，跳出
				break;
			mark[v]=1;//标记已选
			for(i=1;i<=n;i++)
				if(!mark[i])
					lcos[i]=min(lcos[i],map[v][i]);
					//更新lcos的值
		}

		int sum=0;
		for(i=1;i<=n;i++)
			sum+=lcos[i];
		cout<<sum<<endl;
		//输出结果
		return;
	}
	int main()
	{
		int i,j;
		while(cin>>n&&n;)
		{
			for(i=1;i<=n;i++)
				for(j=1;j<=n;j++)
				{
					map[i][j]=INF;
					map[j][i]=INF;
				}
			//初始化map
			char a;
			int an;
			for(i=1;i<n;i++)
			{
				cin>>a>>an;
				while(an--)
				{
					char b;
					int bn;
					cin>>b>>bn;
					map[a-'A'+1][b-'A'+1]=bn;
					map[b-'A'+1][a-'A'+1]=bn;
				}
			}
			prim();
		}
	}