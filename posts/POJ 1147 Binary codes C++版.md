<!--
.. title: POJ 1147 Binary codes C++版
.. slug: poj-1147
.. date: 2013-04-07T05:25:31+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：<[http://poj.org/problem?id=1147](http://poj.org/problem?id=1147)



参考：[http://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform](http://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform)

压缩算法为：给出一个2进制的字符串，依次左移一个数，得到多个字符串，给这些字符串排序，然后输出排列矩阵的最后一竖列

题目要求我们进行解压操作，也就是给我们答案，求给出的2进制字符串。

现开始以为只要排个序就行了，但是只能WA，看了解题报告才懂了一点，算法不介绍了上面讲得很详细了！

代码如下：

	:::cpp
	/*Problem: 1147		User: awq123
	**Memory: 276K		Time: 32MS
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
		int a[3001],b[3001],n,i,j,k;
		cin>>n;
		k=0;
		for(i=1;i<=n;i++)
		{
			cin>>a[i];
			if(a[i]==0)
				k++;
		}
		j=1;
		k++;
		for(i=1;i<=n;i++)
			if(a[i])
				b[k++]=i;
			else
				b[j++]=i;
		k=1;
		for(i=1;i<=n;i++)
		{
			k=b[k];
			cout<<a[k]<<" ";
		}	
	}