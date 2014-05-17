<!--
.. title: POJ 2313 Sequence C++版
.. slug: poj-2313
.. date: 2013-04-07T05:55:06+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2313](http://poj.org/problem?id=2313)


V = (|A(1) – B(1)| + |A(2) – B(2)| + ... + |A(N) – B(N)|) + (|B(1) – B(2)| + |B(2) – B(3)| + ... +|B(N-1) – B(N)|)
将公式简单变形就可以推出b[0]=a[0]和b[n-1]为区间[a[n-1],b[n-2](不知道a[n-1]与b[n-2]大小关系)内的任意一个数或者b[n-1]=a[n-1]和b[0]为区间[a[0],b[1]]区间内的任意一个数,而考虑b[i],即要使 |b[i]-a[i]|+|b[i]-b[i+1]|+|b[i-1]-b[i]|的值最小,即在数轴上找一点满足到点a[i],b[i+1],b[i-1]的距离之和最小，显然该点(即b[i])为这在数轴上三个点中间的一个点(即三个数的中位数),由上面的叙述b[0]已知，现在求b[1],我们可以将a[2]后面的数字暂时去掉，可知这时b[2]=a[2],由b[0],b[2],a[1]这时可以求出b[1],同理求b[2]时采用同样的方法处理。*

代码如下：

	:::cpp
	/*Problem: 2313		User: awq123
	**Memory: 252K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <algorithm>
	using namespace std;
	int solve(int n1,int n2,int n3)
	{
		int s[3];
		s[0]=n1;s[1]=n2;s[2]=n3;
		sort(s,s+3);
		return s[1];
	}

	int main()
	{
		int i,n,num=0,a[101],b[101];
		cin>>n;
		for(i=1;i<=n;i++)
			cin>>a[i];
		b[1]=a[1];b[n]=a[n];
		for(i=2;i<n;i++)
			b[i]=solve(b[i-1],a[i],a[i+1]);
		for(i=1;i<=n;i++)
			num+=abs(a[i]-b[i]);
		for(i=1;i<n;i++)
			num+=abs(b[i]-b[i+1]);
		cout<<num<<endl;
	}
