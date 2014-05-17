<!--
.. title: POJ 2245 Lotto C++版
.. slug: poj-2245
.. date: 2013-04-07T05:40:30+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2245](http://poj.org/problem?id=2245)


解释下题意，给出一个最多13个数的序列，从其中抽出6个数，输出所有的可能序列，按顺序输出。

查了一些资料，最好的方法就是DFS了，平时自己独立做DFS少，就当练习下了。其实我更觉得这样的是简单的递归，也不全算DFS吧。

我的思路是这样的每个数有两种情况，也就是取它和不取它，定义一个函数void dfs(int d,int p)，其中d代表已经取的数目，p代表查看过的数目！这样针对每个情况我们调用两次，分别是取它和不取它，标准dfs其实在取它算完后应该回溯到原样，但是不取它会覆盖这一条数据，也就省了这一步了。

这个题我在结束条件上纠结了下，现开始我用的d==6然后最后一列就不正确了，其实我自己有时利用数组的a[1]做第一个数据，就会总犯一些错误，一些细节的把握不好，最近做题都没有用调试，1是不方便在linux下用，2是递归调试麻烦！

代码不长，因为最近在做短代码的题，代码如下：

	:::cpp
	/*Problem: 2245		User: awq123
	**Memory: 252K		Time: 32MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	using namespace std;

	int n,i,j,a[14],b[7];

	void dfs(int d,int p)//d表示已经搜索到的数也就是深度，p表示搜索过的数
	{
		if(p>n+1)//搜索完，结束
			return;
		if(d==7)//已搜索到6个数，输出
		{
			for(int m=1;m<=6;m++)
				cout<<b[m]<<" ";
			cout<<endl;
			return;
		}
		b[d]=a[p];
		dfs(d+1,p+1);//如果搜索到的结果
		dfs(d,p+1);//没搜索到的结果，b[dep]会自己覆盖
	}

	int main()
	{
		//freopen("input.txt", "r", stdin); 
		while(cin>>n&&n;)
		{
			for(i=1;i<=n;i++)
				cin>>a[i];
			dfs(1,1);
			cout<<endl;
		}
	}
