<!--
.. title: POJ 2159 Ancient Cipher C++版
.. slug: poj-2159
.. date: 2013-04-07T06:42:51+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2159](http://poj.org/problem?id=2159)


解释下题意，通过字母的移位进行加密，但是加密的算法不知道，问是否破解。

比如加密算法是A==>E  C==>B
那么加密AAACC就成为EEEBB，虽然这样的加密算法我们不知道，但是要能破解，那么字母的数量是不便的，比如这个例子中，一共；两种字母数量分别是2  3，那么就能完成一一对应的关系。从而完成加密过程，我们将每个字母的数量记录下然后排序，看是否满足，数量相同。



代码如下：

	:::cpp
	/***************************************
	Problem: 2159		User: awq123
	Memory: 200K		Time: 47MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int a[26],b[26],len1,len2,i;
		char str1[105],str2[105];
		cin>>str1>>str2;
		len1=strlen(str1);
		len2=strlen(str2);
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for(i=0;i<len1;i++)
			a[str1[i]-65]++;
		for(i=0;i<len2;i++)
			b[str2[i]-65]++;
		sort(a,a+26);
		sort(b,b+26);
		for(i=0;i<26;i++)
			if(a[i]!=b[i])
			{
				cout<<"NO"<<endl;
				return 0;
			}
		cout<<"YES"<<endl;
	}