<!--
.. title: POJ 1543 Perfect Cubes C++版
.. slug: poj-1543
.. date: 2013-04-07T08:52:01+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1543](http://poj.org/problem?id=1543)


题意不难，求小于n的数的立方能否写成三个的立方和，水题，暴力枚举！


代码如下：

	:::cpp
	/*Problem: 1543		User: awq123
	**Memory: 256K		Time: 47MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int n,i,j,k,l;
		cin>>n;
		for(i=3;i<=n;i++)
		{
			for(j=2;j<n;j++)
				for(k=j+1;k<n;k++)
					for(l=k+1;l<n;l++)
						if(i*i*i==j*j*j+k*k*k+l*l*l)
						{
							cout<<"Cube = "<<i<<", Triple = ("<<j<<","<<k<<","<<l<<")"<<endl;
							break;
						}
		}
	}
