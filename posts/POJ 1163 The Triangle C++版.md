<!--
.. title: POJ 1163 The Triangle C++版
.. slug: poj-1163
.. date: 2013-04-07T04:47:08+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1163](http://poj.org/problem?id=1163)

这个题目一个数字金字塔，求由上到下，经过的数字和最大为多少，其实本身看着简单的很，第一想法肯定是递归，必定这样的题目我以前做过，老师也是教的递归做法，由上到下，将问题分解为若干个小问题，这样利用一个求值型函数既可解决问题。代码如下：

	:::cpp
	#include <iostream>
	using namespace std;

	int n,num[100][100];

	int DFS(int i, int j)
	{
		if(i==n)
			return num[i][j];
		else if (DFS(i+1,j)>DFS(i+1,j+1))
			return DFS(i+1,j)+num[i][j];
		else
			return DFS(i+1,j+1)+num[i][j];
	}
	int main()
	{
		cin>>n;
		for(int i=1; i<=n; i++)
			for(int k=1; k<=i; k++)
				cin>>num[i][k] ;
		cout<<DFS(1,1)<<endl;
	}

可是无论怎么试都是超时，这样的解决办法应该有问题，查阅解题报告发现本题纯递归运算过大，应该用动态规划解决，改变思路编写新的代码，由下至上，依次求解距离放在每一个数的位置上，其实也就是递归的逆运算，很用以理解，代码如下:

	:::cpp 
	/*Problem: 1163		User: awq123
	**Memory: 292K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	using namespace std;

	int main()
	{
		int i,j,n,num[100][100];
		cin>>n;
		for(i=0; i<n; i++)
			for(j=0; j<=i; j++)
				cin>>num[i][j] ;
		for(i=n-2;i>=0;i--)
			for(j=0;j<=i;j++)
				num[i][j]+=(num[i+1][j]>num[i+1][j+1])?num[i+1][j]:num[i+1][j+1];
		cout<<num[0][0]<<endl;
	}


PS：发点小牢骚，每次做问题都是这样解决的没问题，到了oj系统上就这样那样的调半天，还是对于oj系统本身不了解，有机会还是去研究下原理以及代码运行流程！！