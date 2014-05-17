<!--
.. title: POJ 1386 Play on Words C++版
.. slug: poj-1386
.. date: 2013-04-07T08:52:01+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1386](http://poj.org/problem?id=1386)


解释下题意，给出一组字符串，问是否能将这些字符串首尾相接组成一个长字符串，首尾两个字母一样才能连接。

简化题目，我们只考虑首尾字母，组成的有向欧拉回路，要能够相连，必须全部入度等于出度或者除了两个外其他点的入度等于出度，且不相等的一个入度比出度大1，一个小1！

代码如下：

	:::cpp
	/*Problem: 1386		User: awq123
	**Memory: 252K		Time: 688MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int fa[26];

	int find_set(int x)
	{
		if(fa[x]==x)
			return x;
		fa[x]=find_set(fa[x]);
		return fa[x];
	}
	int main()
	{
		//freopen("Input.txt", "r", stdin);
		int in,out,i,t,n,d1[26],d2[26],vis[26];
		char str[1005];
		cin>>t;
		while(t--)
		{
			memset(d1,0,sizeof(d1));
			memset(d2,0,sizeof(d2));
			memset(vis,0,sizeof(vis));
			cin>>n;
			for(i=0;i<26;i++)
				fa[i]=i;
			while(n--)
			{
				cin>>str;
				in=str[0]-'a',out=str[strlen(str)-1]-'a';
				d1[in]++;
				d2[out]++;
				vis[in]=1;
				vis[out]=1;
				fa[find_set(in)]=find_set(out);
			}
			int flag=1,flag1=0,flag2=0;
			for(i=0;i<26&&flag;i++)
			{
				if(vis[i]&&d1;[i]!=d2[i])
				{
					if(d1[i]==d2[i]+1)
						flag1++;
					else if(d1[i]==d2[i]-1)
						flag2++;
					else
						flag=0;
				}
			}
			for(i=0;i<26;i++)
				if(vis[i]&&find;_set(out)!=find_set(i))
					flag=0;
			if(flag)
			{
				if((flag1==1&&flag2;==1)||(flag1==0&&flag2;==0))
					cout<<"Ordering is possible."<<endl;
			}
			else
				cout<<"The door cannot be opened."<<endl;
		}
	}