<!--
.. title: POJ 1547 Clay Bully C++版
.. slug: poj-1547
.. date: 2013-04-07T08:10:37+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1547](http://poj.org/problem?id=1547)


题意简化为，每人输入长，宽，高，名字，根据每个的体积，输出最大的和最小的名字！

利用结构体储存数据，然后排序输出，不难。我看到有童鞋用map做，表示不会啊，还要慢慢学啊！


代码如下

	:::cpp
	/*Problem: 1547		User: awq123
	**Memory: 244K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	struct node
	{
		int a,b,c,s;
		char name[10];
	}d[10];

	int cmp(node n1,node n2)
	{
		return n1.s<n2.s;
	}

	int main()
	{
		int t,i;
		while(cin>>t&&t;!=-1)
		{
			for(i=0;i<t;i++)
			{
				cin>>d[i].a>>d[i].b>>d[i].c>>d[i].name;
				d[i].s=d[i].a*d[i].b*d[i].c;
			}
			sort(d,d+t,cmp);
			cout<<d[t-1].name<<" took clay from "<<d[0].name<<"."<<endl;
		}


	}