<!--
.. title: POJ 1200 Crazy Search C++版
.. slug: poj-1200
.. date: 2013-04-07T07:55:40+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1200](http://poj.org/problem?id=1200)


解释下题意，一个由nc格字母组成的字符串，求有多少种长度为n的子串！比如
"daababac"就有5种长度为3的字符串"daa"; "aab"; "aba"; "bab"; "bac"

分析下题意，要求分辨子串是否不同，纯字符判断会花很多时间，我们构建一个nc进制的数列，将所有字符转换为0，1，2。。nc-1的数字，求每个子串对应的值是否相同就可以间接反映子串是否相同，

其中ch为字符串，used记录是否出现过，hash分配数字，

代码如下

	:::cpp
	/***************************************
	Problem: 1200		User: awq123
	Memory: 20496K		Time: 79MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	using namespace std;

	bool used[20000000];
	int hash[300];
	char ch[1000000];
	int main()
	{
		int n,nc,count=0,num=0;
		memset(used,0,sizeof(used));
		memset(hash,-1,sizeof(hash));
		scanf("%d%d%s",&n;,&nc;,ch);
		int len=strlen(ch);
		for(int i=0;i<=len-n;i++)
		{
			int sum=0;
			for(int j=i;j<i+n;j++)
			{
				if(hash[ch[j]-'a']==-1)
					hash[ch[j]-'a']=count++;
				sum=nc*sum+hash[ch[j]-'a'];
			}
			if(used[sum]==0)
			{
				used[sum]=1;
				num++;
			}
		}
		cout<<num<<endl;
	}
