<!--
.. title: POJ 2136 Vertical Histogram C++版
.. slug: poj-2136
.. date: 2013-04-07T09:50:22+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1621](http://poj.org/problem?id=1621)


不解释题意了，看了示例输出就知道了，给出输入的四句话的字母分布图

我利用一个num数组统计每个字母出现的次数，然后画图，这题主要有几个问题：
1是读入字符串的时候用cin，半天num数组都有问题，后来调试发现cin不能读入带空格的字符串，果断换回gets，
2是输出*号的时候那个


>if(j%2==1&&(i>max-num[(j-1)/2]))

中的>写成了>=，不过这个错一会就发现了。

总的来说，这个题不难，但是考基本功，以及细心，不要被这样一个简单的题吓到了！

代码如下：

	:::cpp
	/*Problem: 2136		User: awq123
	**Memory: 172K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>

	using namespace std;

	int main()
	{
	    char str[80];
	    int i,j,num[26];
	    //初始化数组
	    for(i=0;i<26;i++)
		num[i]=0;
	    //读入字符串
	    for(i=0;i<4;i++)
	    {
		gets(str);
		int len=strlen(str);
		//逐个分析，利用数组标记
		for(j=0;j<len;j++)
		{
		    if(str[j]>='A'&&str;[j]<='Z')
		        num[str[j]-'A']++;
		}
	    }
	    int max=0;
		//找出最大值，便于后面行数决定
	    for(i=0;i<26;i++)
		if(num[i]>max)
		    max=num[i];
	    //输出*部分
	    for(i=1;i<=max;i++)
	    {
		for(j=1;j<=51;j++)
		{
				//如果是奇数列而且到了计数部分
		    if(j%2==1&&(i>max-num[(j-1)/2]))
		        cout<<"*";
		    else
		        cout<<" ";
		}
		cout<<endl;
	    }
	    //输出下面一行字母
	    for(i=1;i<=51;i++)
		if(i%2==1)
		    cout<<char('A'+(i-1)/2);
		else
		    cout<<" ";
	}