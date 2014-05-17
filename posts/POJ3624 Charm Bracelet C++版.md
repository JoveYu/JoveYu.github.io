<!--
.. title: POJ3624 Charm Bracelet C++版
.. slug: poj3624
.. date: 2013-04-07T09:36:09+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=3624](http://poj.org/problem?id=3624)


标准01背包问题，利用动态规划解题。

大概题意：有n件物品和一个容量为m的背包。第i件物品的重量是c[i]，价值是w[i]。求解将哪些物品装入背包可使这些物品的重量总和不超过背包容量，且价值总和最大。（来自百度百科）

用子问题定义状态：即f[i][v]表示前i件物品恰放入一个容量为v的背包可以获得的最大价值。则其状态转移方程便是：f[i][v]=max{f[i-1][v],f[i-1][v-c[i]]+w[i]} 。 可以压缩空间，f[v]=max{f[v],f[v-c[i]]+w[i]}

这个方程非常重要，基本上所有跟背包相关的问题的方程都是由它衍生出来的。所以有必要将它详细解释一下：“将前i件物品放入容量为v的背包中”这个子问题，若只考虑第i件物品的策略（放或不放），那么就可以转化为一个只牵扯前i-1件物品的问题。如果不放第i件物品，那么问题就转化为“前i-1件物品放入容量为v的背包中”，价值为f[i-1][v]；如果放第i件物品，那么问题就转化为“前i-1件物品放入剩下的容量为v-c[i]的背包中”，此时能获得的最大价值就是f [i-1][v-c[i]]再加上通过放入第i件物品获得的价值w[i]。

转移方程还有点难理解的，改天多研究下。
代码如下：

	:::cpp
	/*Problem: 3624		User: awq123
	**Memory: 364K		Time: 344MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	using namespace std;

	int max(int a,int b)
	{
	    return a>b?a:b;
	}
	int main()
	{
	    //freopen("in.txt", "r", stdin);
	    int c[3500],w[13000],f[13000];

	    int n,m;
	    cin>>n>>m;

	    for(int i=1;i<=n;i++)
		cin>>c[i]>>w[i];

	    for(int i=1;i<=n;i++)
		for(int v=m;v>=c[i];v--)
		    f[v]=max(f[v],f[v-c[i]]+w[i]);

	    cout<<f[m];
	}