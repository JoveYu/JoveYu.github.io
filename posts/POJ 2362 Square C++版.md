<!--
.. title: POJ 2362 Square C++版
.. slug: poj-2362
.. date: 2013-04-07T08:04:01+08:00
.. tags:
.. link:
.. description:
.. type: text
-->


题目链接：[http://poj.org/problem?id=2362](http://poj.org/problem?id=2362)


题目要求我们判断它给出的长度的木棍是否能组成一个正方形。

题目其实类似1011，要说难度，其实没有那个难，因为已经固定了一共四条木棍，但是这题的数据比那题复杂，如果剪枝不好的话，就会TLE，我虽然过了，但是算法应该可以还优化，因为别人有0msAC的。

利用DFS对每种情况，分析，其中num代表已经找到的木棍数，len表示这条边已经完成的长度，原本统一都是从0开始搜索的，可是TLE，后来主要优化了，dfs内的搜索开始位置，每次从i+1开始搜索，如果一条边完了，从0开始搜索，

其中有个小细节，就是降序排列，能省一些功夫，。

代码如下：

	:::cpp
	/***************************************
	Problem: 2362		User: awq123
	Memory: 164K		Time: 110MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	bool used[25];
	int d[25],n,side;

	int cmp(int a,int b)
	{
		return a>b;
	}

	bool dfs(int begin,int num,int len)
	{
		if(len==side&&num;==n)
			return 1;
		if(len==side)
			len=0;
		for(int i=begin;i<n;i++)
		{
			if(i&&d;[i]==d[i-1]&&used;[i-1]==0)
				continue;
			if(d[i]<side-len&&used;[i]==0)
			{
				used[i]=1;
				if(dfs(i+1,num+1,len+d[i]))
					return 1;
				used[i]=0;
			}
			if(d[i]==side-len&&used;[i]==0)
			{
				used[i]=1;
				if(dfs(0,num+1,len+d[i]))
					return 1;
				used[i]=0;
			}
		}
		return 0;
	}

	int main()
	{
		int t,sum;
		scanf("%d",&t;);
		while(t--)
		{
			sum=0;
			scanf("%d",&n;);;
			for(int i=0;i<n;i++)
			{
				scanf("%d",&d;[i]);
				sum+=d[i];
			}
			if(sum%4)
			{
				printf("non");
				continue;
			}
			side=sum/4;
			sort(d,d+n,cmp);
			memset(used,0,sizeof(used));
			if(dfs(0,0,0))
				printf("yesn");
			else
				printf("non");
		}
	}