<!--
.. title: POJ 1503 Integer Inquiry C++版
.. slug: poj-1503
.. date: 2013-04-07T07:57:41+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1503](http://poj.org/problem?id=1503)


高精度加法，要求输出所有输入的数的和；

100位的数，无法用变量储存，解题方法不难，简单模拟加法的过程；也就是满10进位的方法，我们利用数组，储存每一位数，然后由个位开始相加在加上上一位的进位数，得出这个位上的数，和下一个进位数，其中有一点需要注意，也是我一直WA的一个地方，

	:::cpp
	num[num[0]+1]+=jw;

所有位数计算后，还有一个进位数，要加到后一位里，这个测试数据也巧，没有这句话也能输出，因为第一位是1

我用的数组的第一位数储存，字符串长度，

代码如下：

	:::cpp
	/***************************************
	Problem: 1503		User: awq123
	Memory: 232K		Time: 0MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	using namespace std;

	int main()
	{
		int i,j,jw,sum,num[105];
		char str[105];
		memset(num,0,sizeof(num));
		while(1)
		{
			cin>>str;
			if(strcmp(str,"0")==0)
				break;
			num[0]=strlen(str);
			jw=0;sum=0;
			for(j=1;j<=num[0];j++)
			{
				sum=num[j]+str[num[0]-j]-'0'+jw;
				num[j]=sum%10;
				jw=sum/10;
			}
			num[num[0]+1]+=jw;
		}
		int flag=0;
		for(i=104;i>=1;i--)
		{
			if(num[i]!=0)
				flag=1;
			if(flag==1)
				cout<<num[i];
		}
		cout<<endl;
	}
