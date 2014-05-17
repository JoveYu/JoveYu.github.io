<!--
.. title: POJ 1080 Human Gene Functions C++版
.. slug: poj-1080
.. date: 2013-04-07T06:39:03+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1080](http://poj.org/problem?id=1080)


不错的DP题，做了好多DP了，越做越觉得DP思路真的很开阔，以后还要加强，这题我参考的别人的解题报告，加以自己的想法。

解释下题意，两个字符串，通过增加空格来调整字符串，使得对应字符得到的数相加最大，比如题目中的  
AGTGATG   
-GTTA-G   
第二列解释通过增加两个空格才和第一列对应的，一一对应关系参照  



![1080](http://poj.org/images/1080/1080_1.gif)

可得到最大的得分(-3)+5+5+(-2)+5+(-1) +5=14

我们可以看到，相同的字符是得分最大的，那么我们可以想到LCS问题，这题也算是LCS的一种变形。
解释下DP思路，dp[i][j]记录第一列i个字符和第2列j个字符开始的最大得分，这个得分也就是前面可能的三种情况的最大值！我们来举个例子：
比如i和j分别指字符G，C
那么有三种情况：  
GXXX  
CXXX  
那么dp[i][j]=dp[i-1][j-1]+getmatch(str1[i-1],str2[j-1])  
-GXX  
CXXX  
那么dp[i][j]=dp[i][j-1]+getmatch(str2[j-1],'-')  
GXXX  
-CXX  
那么dp[i][j]=dp[i-1][j]+getmatch(str1[i-1],'-')  
这样由dp[0][0]开始动态规划下去就是了，其中还要注意i，j分别等于0的情况，一面i-1，j-1不存在。

代码种getnum函数将字符转换数字getmatch将组合转换成得分

具体见代码：

	:::cpp
	/***************************************
	Problem: 1080		User: awq123
	Memory: 292K		Time: 16MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int mymax(int a,int b,int c)
	{
		int temp=a>b?a:b;
		return temp>c?temp:c;
	}

	int match[5][5]=
	{
		{5,-1,-2,-1,-3},
		{-1,5,-3,-2,-4},
		{-2,-3,5,-2,-2},
		{-1,-2,-3,5,-1},
		{-3,-4,-2,-1,0}
	};

	int getnum(char ch)
	{
		switch (ch)
		{
			case 'A':return 0;
			case 'C':return 1;
			case 'G':return 2;
			case 'T':return 3;
			case '-':return 4;
			default:return 5;
		}
	}

	int getmatch(char ch1,char ch2)
	{
		return match[getnum(ch1)][getnum(ch2)];
	}

	int main()
	{
		int t,len1,len2,dp[105][105],i,j;
		char str1[105],str2[105];
		cin>>t;
		while(t--)
		{
			cin>>len1>>str1>>len2>>str2;
			dp[0][0]=0;
			for(i=1;i<=len1;i++)
				dp[i][0]=dp[i-1][0]+getmatch(str1[i-1],'-');
			for(j=1;j<=len2;j++)
				dp[0][j]=dp[0][j-1]+getmatch(str2[j-1],'-');
			for(i=1;i<=len1;i++)
				for(j=1;j<=len2;j++)
					dp[i][j]=
					mymax(
						dp[i][j-1]+getmatch(str2[j-1],'-'),
						dp[i-1][j]+getmatch(str1[i-1],'-'),
						dp[i-1][j-1]+getmatch(str1[i-1],str2[j-1])
					);
			cout<<dp[len1][len2]<<endl;
		}
	}