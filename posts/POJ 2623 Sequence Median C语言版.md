<!--
.. title: POJ 2623 Sequence Median C语言版
.. slug: poj-2623
.. date: 2013-04-07T09:34:41+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2623](http://poj.org/problem?id=2623)


这个题目不难，基本的快速排序，算法可以参考我的一篇文章《快速排序的C++表现》，但是还是有两个小细节是我没注意到的：

1：44行我原本有那个的float型的可以一直WA，不知道为什么，后来参考别人的代码才发现用double就好了，
2：文章中输出有这样一句要求：

>You should print the value of the median with exactly one digit after decimal point.

就算是整数，也要保留一位小数，也就是在后面输出个“.0”

下回要注意审题了，呵呵！

代码如下：

	:::cpp
	/*Problem: 2623		User: awq123
	**Memory: 1156K		Time: 250MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	using namespace std;

	int num[250020];
	void quicksort(int s,int e)
	{
		if(e-s<1)
			return;
		int i=s,j=e;
		int tmp=num[s];
		while(i<j)
		{
			while(i<j&&num;[j]>tmp)
				j--;
			if(j>i)
				num[i++]=num[j];
		
			while(i<j&&num;[i]<tmp)
				i++;
			if(i<j)
				num[j--]=num[i];
		}
		num[i]=tmp;
		quicksort(s,i-1);
		quicksort(i+1,e);
	}

	int main()
	{
		//freopen("in.txt", "r", stdin);
		int n;
		scanf("%d",&n;);
		for(int i=0;i<n;i++)
			scanf("%d",&num;[i]);
		quicksort(0,n-1);
		//for(int i=0;i<n;i++)
			//printf("%d ",num[i]);
		if(n%2==0)
			printf("%0.1lf",((double)num[n/2]+(double)num[n/2-1])/2.0);
		else
			printf("%d.0",num[n/2]);
	}