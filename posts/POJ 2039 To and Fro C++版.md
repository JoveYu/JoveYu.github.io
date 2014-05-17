<!--
.. title: POJ 2039 To and Fro C++版
.. slug: poj-2039
.. date: 2013-04-07T09:42:02+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2039](http://poj.org/problem?id=2039)


解释下题意，一个简单的字符串加密解密实现，给出了算法，让你实现，这里是给出一个数字和加密的字符串让你解密。

解释下加密算法，将字符串写成一个矩阵，依次由上到下，由左到又，加密后的字符串就是横着读的结果，单数行正着读，双数行反着读。这里搞懂了就不难了，这样的题难在矩阵参数的判断。

前面我也纠结了好久那个矩阵的排布，这里我建议先用笔在纸上，先花好理解好其关系，在来解题不急。

代码如下：

	:::cpp
	/*Problem: 2039		User: awq123
	**Memory: 248K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <string.h>
	using namespace std;

	int main()
	{
	    int n,m;
	    char data[205][25],str[205];
	    while(cin>>n)
	    {
		if(n==0)
		    break;
		cin>>str;
		int l=strlen(str);
		m=l/n;
		for(int i=0;i<l;i++)
		{
		    if((i/n)%2==0)
		        data[i/n][i%n]=str[i];
		    else
		        data[i/n][n-1-i%n]=str[i];
		}
		for(int i=0;i<n;i++)
		{
		    for(int j=0;j<m;j++)
		        cout<<data[j][i];
		}
		cout<<endl;
	    }
	}
