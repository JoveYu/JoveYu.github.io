<!--
.. title: POJ 1575 Easier Done Than Said? C++版
.. slug: poj-1575
.. date: 2013-04-07T08:12:07+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1575](http://poj.org/problem?id=1575)


题意让我们判断所给的字符串是否满足所给的条件：
1，至少有一个元音字母
2，不能出现三个元音连续或者三个辅音连续
3，除了ee和oo不能出现两格字母连续

我用j1，j2，j3分别判断这三个条件，其中j2的if语句还是写得有点特色的，看是否三个或和三个且的值一样，嘿嘿


具体见代码：

	:::cpp
	/*Problem: 1575		User: awq123
	**Memory: 200K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	char ch[25];
	int len;

	bool y(char q)
	{
		if (q=='a'||q=='e'||q=='i'||q=='o'||q=='u')
			return 1;
		return 0;
	}

	bool j1()
	{
		for(int i=0;i<len;i++)
			if(y(ch[i]))
				return 1;
		return 0;
	}

	bool j2()
	{
		if(len<3)
			return 1;
		for(int i=0;i<=len-3;i++)
			if((y(ch[i])&&y;(ch[i+1])&&y;(ch[i+2]))==(y(ch[i])||y(ch[i+1])||y(ch[i+2])))
				return 0;
		return 1;
	}

	bool j3()
	{
		if(len<2)
			return 1;
		for(int i=0;i<=len-2;i++)
			if((ch[i]==ch[i+1])&&ch;[i]!='e'&&ch;[i]!='o')
				return 0;
		return 1;
	}

	int main()
	{
		while(cin>>ch)
		{
			if(strcmp(ch,"end")==0)
				break;
			len=strlen(ch);
			cout<<"<"<<ch<<"> is ";
			if(!(j1()&&j2;()&&j3;()))
				cout<<"not ";
			cout<<"acceptable."<<endl;
		}
	}