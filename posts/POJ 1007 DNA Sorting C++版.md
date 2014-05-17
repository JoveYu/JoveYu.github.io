<!--
.. title: POJ 1007 DNA Sorting C++版
.. slug: poj-1007
.. date: 2013-04-07T06:42:09+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1007](http://poj.org/problem?id=1007)


简单排序题，要求我们根据逆序对的数量进行升序排序排序！

解释下逆序对，我也是刚接触这么个概念的，比如一列数3 4 2 5 1 那么在后面的数比前面小就是一组，32 42 51 31 41 21 51 ，

通过结构体来整体排序会简单点，不过要自己编写cmp函数，当然自己还是比较熟练了。



代码如下：

	:::cpp
	/***************************************
	Problem: 1007		User: awq123
	Memory: 244K		Time: 16MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	typedef struct dna
	{
		int n;
		char ch[55];
	}DNA;

	int cmp(DNA a,DNA b)
	{
		return a.n<b.n;
	}

	int main()
	{
		DNA d[105];
		int i,j,k,n,m;
		cin>>n>>m;
		for(i=0;i<m;i++)
		{
			cin>>d[i].ch;
			d[i].n=0;
			for(j=0;j<n;j++)
				for(k=j+1;k<n;k++)
					if(d[i].ch[j]>d[i].ch[k])
						d[i].n++;
		}
		sort(d,d+m,cmp);
		for(i=0;i<m;i++)
			cout<<d[i].ch<<endl;
	}