<!--
.. title: POJ 3210 Coins C++版
.. slug: poj-3210-coins-c
.. date: 2013-04-07T08:16:30+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1006](http://poj.org/problem?id=1006)


解释下题意，Snoopy想问下，若有n枚硬币，这n枚硬币的初始状态是任意的，则至少需要翻转几次，才能保证对于任何一种初始状态而言，都能变成n枚硬币全为正或全为反。

分析：

1：若为偶数

那么正反数目就有奇奇和偶偶两种情况，很明显奇数的翻转不适合偶数，偶数的翻转不适合奇数  
例如： ○○●●●●  则翻转 2,4,6,8……次均可。  
例如： ○○○○○●  则翻转 1,3（先将●翻为○，再将任一个○翻两下）,5,7……次均可。  

2：若为奇数  
若所有硬币一开始就同一面向上那么翻转次数一定为偶数，那么对于其他情况，我们必须翻转偶数面来完成目标
例如： ○○○○●●●  则翻转4,6,8,10……次均可，其中最小为4。要保证对7枚硬币的任意初始状态都可行，则最小应为 7-1=6  
这样我们就能推出，至少应该翻转n-1次


代码如下：

	:::cpp
	/*Problem: 3210		User: awq123
	**Memory: 244K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int n;
		while (cin>>n&&n;)
		{
			if (n%2==0)
				cout<<"No Solution!"<<endl;
			else
				cout<<n-1<<endl;	
		}
	}
