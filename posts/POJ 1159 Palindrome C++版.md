<!--
.. title: POJ 1159 Palindrome C++版
.. slug: poj-1159
.. date: 2013-04-07T08:36:21+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1159](http://poj.org/problem?id=1159)


题目问，在一个字符串里至少加几个字母能组成回文词，所谓回文词，就是反着读和正着一样的字符串，以输入例子来看  
Ab3bd  
可以变成  
Adb3bdA  
也可以变成  
dAb3bAd  
虽然答案不唯一，但是增加的数量是有限的。  

我们利用DP解这题，具体思路是，由字符串两端开始比较，若两格字母相同，那么同时去掉这两个的话，答案是不变的，若不同，就由两种情况，分别是在左边加上右边的字母，或者在右边加上左边的字母，我们取两中情况的最小值，然后递归调用下去，用dp[i][j]表示左边第i个开始，和右边第j个开始的最小数量

DP思路简化为：

	:::cpp
	if(str[i]==str[j])
		dp[i][j]=dp[i+1][j-1];
	else
		dp[i][j]=min(dp[i][j-1],dp[i+1][j])+1;


PS：这题，还有个点要注意，就是不能用int的数组，会超内存限制的，用short刚刚好！

代码如下：

	:::cpp
	/*Problem: 1159		User: awq123
	**Memory: 49332K		Time: 532MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	using namespace std;

	short min(short a,short b)
	{
		return a>b?b:a;
	}
	short dp[5005][5005];

	int main()
	{
		short len,i,j;
		char str[5005];
		cin>>len>>str;
		memset(dp,0,sizeof(dp));
		for(i=len-2;i>=0;i--)
			for(j=i+1;j<len;j++)
			{
				if(str[i]==str[j])
					dp[i][j]=dp[i+1][j-1];
				else
					dp[i][j]=min(dp[i][j-1],dp[i+1][j])+1;
			}
		cout<<dp[0][len-1]<<endl;
	}