<!--
.. title: POJ 2407 Relatives C++版
.. slug: poj-2407
.. date: 2013-04-07T08:44:03+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1048](http://poj.org/problem?id=1048)


题意，求小于n的数中和n互质的数的个数！

这题，我先开始的思路是针对每个小于n的数求最大公约数，但是用辗转相除法，递归层数过高！后来想开个数组，标记互质的数，但是n太大，无法开出来，搜索了一下，有一个函数，是用来解决这一问题的，就是欧拉函数，我参看[维基百科](http://zh.wikipedia.org/wiki/%E6%AC%A7%E6%8B%89%E5%87%BD%E6%95%B0)，写出算法！

欧拉函数的求解，可以简化为，将n写成a1^n1*a2^n2....an^nn的形式，那么这个数的欧拉函数表达式为a1^(n1-1)*(a1-1)  *  a1^(n2-1)*(a1-1)....

还不懂的去看看维基百科！


代码如下：


	:::cpp
	/*Problem: 2407		User: awq123
	**Memory: 260K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <cmath>
	using namespace std;

	int main()
	{
		int n,i,num;
		while(cin>>n&&n;)
		{
			num=1;
			for(i=2;i<=n;i++)
			{
				int t=0;
				while(n%i==0)
				{
					t++;
					n/=i;
				}
				if(t!=0)
					num*=(pow((float)i,t-1)*(i-1));
			}
			cout<<num<<endl;
		}
	}
