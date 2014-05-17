<!--
.. title: POJ 1207 The 3n + 1 problem C++版
.. slug: poj-1207
.. date: 2013-04-07T05:05:43+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1207](http://poj.org/problem?id=1207)

一个看似复杂的题目，其实算法都已经给出，要求你求出i到j之间最大循环次数，水题，最近做的水题还真是多，没办法东西还是要一点点的学，这个题目不难但是有个小细节需要掌握，就是输入i  j   时若i>j那么要从j开始算，现开始我完成代码也不知道什么问题，后来看了解题报告才知道的！！


代码如下：

	:::cpp
	/*Problem: 1207		User: awq123
	**Memory: 252K		Time: 16MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	using namespace std;

	int main()
	{
		int a,b,i,j,m,key,t,max;
		while(cin>>a>>b)
		{
		
			i=a;j=b;
			if(i>j)
			{
				t=i;i=j;j=t;
			}
			max=0;
			for(m=i;m<=j;m++)
			{
				t=1;
				key=m;
				while(key!=1)
				{
					if(key%2)
						key=3*key+1;
					else
						key=key/2;
					t++;;
				}
				if(t>max)
					max=t;
			}
			cout<<a<<" "<<b<<" "<<max<<endl;
		}
	}