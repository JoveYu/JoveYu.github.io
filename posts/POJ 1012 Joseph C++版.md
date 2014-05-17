<!--
.. title: POJ 1012 Joseph C++版
.. slug: poj-1012
.. date: 2013-04-07T06:16:14+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1012](http://poj.org/problem?id=1012)


经典的约瑟夫问题的变形，什么？约瑟夫问题是什么？来，哥给你个[传送门](http://baike.baidu.com/view/213217.htm)

解释下题意，有k个好人和k个换人依次围成一个环，从第一个人开始数，数到m杀掉这个人，问m为多少，使坏人都在好人前面死


由于数据量不大，如果你自己已经打好表，那么有种简单的方法，纯粹为了0MSAC，代码如下：

	:::cpp
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int Joseph[]={0,2,7,5,30,169,441,1872,7632,1740,93313,459901,1358657,2504881,1245064};
		int k;
		while(cin>>k&&k;)
			cout<<Joseph[k]<<endl;
	}

但是如果纯粹计算的话，利用递推公式

	:::cpp
	p[i]=(p[i-1]+m-1)%(n-i+1);//p[i]为第i个杀的人n=2*k,m为所求！


公式需要推，有耐心的朋友可以自己试试，主要就是每次过后将编号排列好！


由于oj系统反复利用这15组数据解题，打表，以避免超时

完整代码如下

	:::cpp
	/*Problem: 1012		User: awq123
	**Memory: 248K		Time: 266MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int joseph[14]={0},p[29];
		int k,n,m,i;
		while(cin>>k&&k;)
		{
			if(joseph[k])
			{
				cout<<joseph[k]<<endl;
				continue;
			}
			n=2*k;
			m=1;
			memset(p,0,sizeof(p));
			for(i=1;i<=k;i++)
			{
				p[i]=(p[i-1]+m-1)%(n-i+1);
				if(p[i]<k)
				{
					i=0;
					m++;
				}
			}
			joseph[k]=m;
			cout<<joseph[k]<<endl;
		}
	}
