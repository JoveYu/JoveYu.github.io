<!--
.. title: POJ 1281 MANAGER C++版
.. slug: poj-1281
.. date: 2013-04-07T06:31:13+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1281](http://poj.org/problem?id=1281)

解释下题意，先输入最大的数，再输入最后查询移出数的个数，依次输入查询移出数的位置，后面就是循环的操作了；

* a：加入一个数
* p：设置p的值
* r：删除一个数，p为1删除最小的数，p为2删除最大的数！
* e：结束一个输入

我们以给出的例子来分析

>Sample Input  
5  
2  
1 3  
a 2  
a 3  
r  
a 4  
p 2  
r  
a 5  
r  
e  

最大值设为5，后面要查询两个数，分别是第1个和第3个，然后开始循环
a2a3---现在列表为2，3  
r------p为1，删除最小的，现在列表为3，移出列表为2  
a4-----现在列表为3，4，移出列表为2  
p2-----p设为2  
r------p为2，删除最大的，现在列表为3，移出列表为2，4  
a5-----现在列表为3，5，移出列表为2，4  
r------p为2，删除最大的，现在列表为3，移出列表为2，4，5  
e------结束  

然后输出第1个和第3个移出的，既2，5。

模拟题没什么好说的，他说什么你就干什么，利用数组inum记录查询的位置，inow记录现在数列里的数，idel记录删除的数，用inumx，inowx，idelx分别记录每个数组里的数的个数。话不多说看代码，很好理解。

代码如下：

	::cpp
	/***************************************
	Problem: 1281		User: awq123
	Memory: 700K		Time: 0MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	#include <cmath>
	using namespace std;

	int cmp(int a,int b)
	{
		return a>b;
	}

	int main()
	{
		int inum[10000],inow[10000],idel[100000];
		int imax,i,p,inumx,inowx,idelx;
		char judge;
		while(cin>>imax>>inumx)
		{
			p=1,inowx=0,idelx=0;
			for(i=0;i<inumx;i++)
				cin>>inum[i];
			while(1)
			{
				cin>>judge;
				if (judge=='e')
					break;
				else if (judge=='a')
				{
					cin>>inow[inowx];
					inowx++;
				}
				else if (judge=='r')
				{
					if(p==1)
						sort(inow,inow+inowx,cmp);
					else if(p==2)
						sort(inow,inow+inowx);
					inowx--;
					idel[idelx]=inow[inowx];
					idelx++;
				}
				else if (judge=='p')
				{
					cin>>p;
				}

			}
			for (i = 0; i < inumx; i++)
			{
				if(inum[i]>idelx)
					cout<<-1<<endl;
				else
					cout<<idel[inum[i]-1]<<endl;
			}
			cout<<endl;
		}
	}