<!--
.. title: POJ 2211 Photograph C++版
.. slug: poj-2211-photograph-c
.. date: 2013-04-07T05:29:29+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2211](http://poj.org/problem?id=2211)


先解释下题意，由n个人一起合影，每张照片可以容下k个人，问给出的排列是第几个照相的，也就是排列问题。

比如第三个例子

>3 3    
>1 2 3

那么只用照一次就够了

比如给出数据

>3 2   
>3 2

那么照相的顺序为

>1 2  
>1 3  
>2 1  
>2 3  
>3 1  
>3 2

所以输出为6

讲下思路，我也是在discuss里看的，没想到有这么简单的思路，这个方法应该用的是贪心。
首先利用数组输入数据，然后由第一个数开始依次判断，假设这个数为t那么前面的t-1个数的情况都是完整的全排列，比如第四个例子是一个5 3的数据，第一个数5，那么前面可能的数1 2 3 4，都有全排列的种数，每种4×3。
关键是接下来的思路，对后面的数扫描如果大于t那么都减去1，这样从下一个开始就转化为了一个4 2的数据，每次只判断第一个的全排列，一直到最后，所有的加起来就是所有的排列数了！

原来排列都是通过先排列在计数的方式，时间慢，切复杂，这个题给了我全新的思路，强烈推介下，虽然代码不长，但绝对的好题！

代码如下：

	:::cpp
	/*Problem: 2211		User: awq123
	**Memory: 252K		Time: 141MS
	**Language: C++		Result: Accepted
	*/
	#include <cstdio>
	#include <iostream>
	#include <cstring>
	#include <algorithm>
	#include <cmath>
	using namespace std;

	int main()
	{
		int t,n,i,j,k,num,temp,m,a[13];
		cin>>t;
		for(i=1;i<=t;i++)
		{
			cin>>n>>k;
			num=1;
			for(j=1;j<=k;j++)
				cin>>a[j];
			for(j=1;j<=k;j++)
			{
				temp=a[j]-1;
				for(m=n-j;m>=n-k+1;m--)
					temp*=m;
				num+=temp;
				for(m=j+1;m<=k;m++)
					if(a[m]>a[j])
						a[m]--;		
			}
			cout<<"Variace cislo "<<i<<" ma poradove cislo "<<num<<"."<<endl;
		}
	}