<!--
.. title: POJ 1011 Sticks C++版
.. slug: poj-1011
.. date: 2013-04-07T06:12:04+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1011](http://poj.org/problem?id=1011)


解释下题意，一些小木棒是一些同样长的大木棒折断成的，求大木棒的最小长度

比如1 2 3 4
就是由两根5折断成的！

简单DFS但是我做了半天都是超时，原因是自己的dfs是处理型的算法上不够简洁，处理过多，递归层数有点大，然后一直TLE，没办法后来借鉴别人的才AC，其中的剪枝有些技巧，比如对于木棒长度的控制，以及剩余长度的控制，还有就是像前面如果有个同样大的数，没有成功的话，那么这个数的情况久不用考虑的，等等，

先上我原来TLE的代码：

	:::cpp
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>

	using namespace std;

	int d[70],used[70],len,n,sum,ok;

	bool cmp(int a,int b)
	{
	 return a>b;
	}

	void dfs(int a,int b,int c)
	{
		if(ok==1)
			return;
		else if(a==n+1)
			return;
		else if(c>sum||b>len)
			return;
		else if(c==sum&&b;==len)	
			ok=1;
		else if(b==len)
			dfs(0,0,c);
		else if(used[a+1]==1)
			dfs(a+1,b,c);
		else
		{
			used[a+1]=1;
			dfs(a+1,b+d[a+1],c+d[a+1]);
			used[a+1]=0;
			dfs(a+1,b,c);
		}
	}

	int main()
	{
		int i;
		while(cin>>n&&n;)
		{
			sum=0;ok=0;
			d[0]=0;
			for(i=1;i<=n;i++)
			{
				cin>>d[i];
				sum+=d[i];
			}
			sort(d+1,d+1+n,cmp);
			for(i=d[1];i<=sum;i++)
			{
				if(ok==1)
					break;
				if(sum%i==0)
				{
					memset(used,0,sizeof(used));
					len=i;
					dfs(0,0,0);
				}
			}
			cout<<len<<endl;
		
		}
	}

其实思路都是一样的，我逐个取，但没有求值型的dfs来的快。以后自己咬多学着点！

再来看看AC的代码，代码如下

	:::cpp
	/*Problem: 1011		User: awq123
	**Memory: 164K		Time: 63MS
	**Language: C++		Result: Accepted
	*/
	#include <stdio.h>
	#include <stdlib.h>
	int sticks[100],n;
	bool used[100];
	int cmp(const void *x,const void *y)
	{
	    return *(int *)y - *(int *)x;
	}
	bool find(int left,int num,int len)
	{
	    int i;
	    if(left == 0 && num == 0)
	    return 1;
	    if(left == 0)
	    left = len;
	    for(i = 0;i < n;i ++)
	    {
		if(sticks[i] <= left && !used[i])
		{
		    used[i] = 1;
		    if(find(left - sticks[i],num-1,len))
		    return 1;
		    used[i] = 0;
		    if(sticks[i] == left || left == len)
		    return 0;
		}
	    }
	    return 0;
	}

	int main()
	{
	    int i,sum = 0;
	    while(scanf("%d",&n;) != EOF && n)
	    {
		sum = 0;
		for(i = 0;i < n;i ++)
		{
		    scanf("%d",&sticks;[i]);
		    sum += sticks[i];
		    used[i] = 0;
		}
		qsort(sticks,n,sizeof(int),cmp);
		for(i = sticks[0];i <= sum;i ++)
		{
		    if((sum % i == 0) && find(i,n,i))
		    {
		        printf("%dn",i);
		        break;
		    }
		}
	    }
	    return 0;
	}