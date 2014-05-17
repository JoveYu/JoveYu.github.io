<!--
.. title: POJ 1029 False coin C++版
.. slug: poj-1029
.. date: 2013-04-07T06:26:28+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1029](http://poj.org/problem?id=1029)


解释下题意，有一些硬币，又一枚是假的重量跟其他的不一样，通过多次称量，求出这个的编号

这个题和1013几乎一模一样，不同的是，1013题目一定可以求出结果，这个不能，不过也就是多了一个判断罢了，还是差不多！

大家可以参考   POJ 1013 Counterfeit Dollar C++版

思路就不说了，跟1013一样！懒一下拉！

代码如下：

	:::cpp
	/***************************************
	Problem: 1029		User: awq123
	Memory: 272K		Time: 32MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int i,j,len,n,k,d[1005],temp[1005],left[505],right[505];
		char cmp[5];
		memset(d,0,sizeof(d));
		cin>>n>>k;
		while(k--)
		{
			cin>>len;
			for (i = 0; i < len; i++)
				cin>>left[i];
			for (i = 0; i < len; i++)
				cin>>right[i];
			cin>>cmp;
			if(cmp[0]=='=')
			{
				for(j=0;j<len;j++)
				{
					d[left[j]]=1;
					d[right[j]]=1;
				}
			}
			else if(cmp[0]=='>')
			{
				memset(temp,0,sizeof(temp));
				for(j=0;j<len;j++)
				{
					if(d[left[j]]==-1)
						d[left[j]]=1;
					else if(d[left[j]]==0)
						d[left[j]]=2;
					if(d[right[j]]==2)
						d[right[j]]=1;
					else if(d[right[j]]==0)
						d[right[j]]=-1;
					temp[left[j]]=1;
					temp[right[j]]=1;
				}
				for(j=0;j<=n;j++)
					if(temp[j]==0)
						d[j]=1;
			}
			else if(cmp[0]=='<')
			{
				memset(temp,0,sizeof(temp));
				for(j=0;j<len;j++)
				{
					if(d[left[j]]==2)
						d[left[j]]=1;
					else if(d[left[j]]==0)
						d[left[j]]=-1;
					if(d[right[j]]==-1)
						d[right[j]]=1;
					else if(d[right[j]]==0)
						d[right[j]]=2;
					temp[left[j]]=1;
					temp[right[j]]=1;
				}
				for(j=0;j<=n;j++)
					if(temp[j]==0)
						d[j]=1;
			}
		}
		int count=0,answer;
		for (i = 1; i <=n ; i++)
		{
			if(d[i]!=1)
			{
				count++;
				answer=i;
			}
		}
		if (count==1)
			cout<<answer<<endl;
		else
			cout<<0<<endl;

	}