<!--
.. title: POJ 1504 Adding Reversed Numbers C++版
.. slug: poj-1504
.. date: 2013-04-07T07:36:56+08:00
.. tags:
.. link:
.. description:
.. type: text
-->


题目链接：[http://poj.org/problem?id=1504](http://poj.org/problem?id=1504)

题意不难，就是将两个数逆序排列，相加，再逆序输出，比如123和456，就应该是321+654=975，那么输出579.

其实这题用字符串的操作函数会方便很多atoi函数，但是自己动手编写简单的函数，还有又用的，我们来看看atoi函数：

	:::cpp
	//int atoi(const char *nptr);
	char a[5]="1234";
	printf("%d",atoi(a)+1);
	//输出1235



代码如下：

	:::cpp
	/***************************************
	Problem: 1504		User: awq123
	Memory: 248K		Time: 63MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	void swap(char* str)
	{
		char temp[100];
		int i,len;
		len=strlen(str);
		strcpy(temp,str);
		for(i=0;i<len;i++)
			*(str+i)=temp[len-1-i];
	}

	int main()
	{
		char str1[100],str2[100];
		int num1,num2,num3,num4,len1,len2,t,i;
		cin>>t;
		while(t--)
		{
			cin>>str1>>str2;
			swap(str1);
			swap(str2);
			len1=strlen(str1);
			len2=strlen(str2);
			num1=0;
			num2=0;
			num4=0;
			for(i=0;i<len1;i++)
				num1=10*num1+str1[i]-'0';
			for(i=0;i<len2;i++)
				num2=10*num2+str2[i]-'0';
			num3=num1+num2;
			while(num3!=0)
			{
				num4=10*num4+num3%10;
				num3/=10;
			}
			cout<<num4<<endl;
		}
	}