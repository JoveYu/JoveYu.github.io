<!--
.. title: POJ 1775 Sum of Factorials C++版
.. slug: poj-1775
.. date: 2013-04-07T09:05:54+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1775](http://poj.org/problem?id=1775)


不难，解释下题意 判断一个数是否能写为多个阶乘的和 

先打表，计算出0-9的阶乘，然后深搜每一个数的组合，其中回溯的方式表示成了||这样搜索不算效率，也能AC！

不过有一点，我没注意，就是0的情况，害我WA了半天，加上个排除就好了！

代码如下：

	:::cpp
	/*Problem: 1775		User: awq123
	**Memory: 216K		Time: 500MS
	**Language: C++		Result: Accepted
	*/
	#include <IOSTREAM>
	using namespace std;

	int num[10]={1,1,2,6,24,120,720,5040,40320,362880};

	int dfs(int n,int i)
	{
		if(n==0)
			return 1;
		if(n<0)
			return 0;
		if(i>9)
			return 0;
		return dfs(n-num[i],i+1)||dfs(n,i+1);
	}

	int main()
	{
		int n;
		while(cin>>n&&n;>=0)
		{
			if(n==0)
				cout<<"NO"<<endl;
			else if(dfs(n,0))
				cout<<"YES"<<endl;
			else
				cout<<"NO"<<endl;
		}

	}
