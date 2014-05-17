<!--
.. title: POJ 1887 Testing the CATCHER C++版
.. slug: poj-1887
.. date: 2013-04-07T09:51:14+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1887](http://poj.org/problem?id=1887)


最长下降序列问题。和最长上升序列类似，有多种方法，我这里用动态规划解题，动态转移方程如下

>dp[i]=max(dp[j])+1,(j∈[1, i-1]);

这里，思路就是用dp数组，记录到每一位的最长下降序列，然后输出其中最大的，详细看代码吧

	:::cpp
	/*Problem: 1887		User: awq123
	**Memory: 288K		Time: 47MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>

	using namespace std;

	int main()
	{
	    int tmp,num[5005],dp[5005],n=1;
	    while(cin>>tmp)
	    {
		if(tmp==-1)
		    break;
		num[1]=tmp;
		int i,j,count=2;
		while(1)
		{
		    cin>>num[count];
		    if(num[count]==-1)
		        break;
		    count++;
		}
		int max=0;
		for(i=1;i<count;i++)
		{
		    dp[i]=1;
		    for(j=1;j<i;j++)
		    {
		        if(num[i]<num[j]&&dp;[i]<dp[j]+1)
		            dp[i]=dp[j]+1;
		    }
		    if(dp[i]>max)
		        max=dp[i];
		}
		cout<<"Test #"<<n<<":"<<endl;
		cout<<"  maximum possible interceptions: "<<max<<endl<<endl;
		n++;
	    }
	}