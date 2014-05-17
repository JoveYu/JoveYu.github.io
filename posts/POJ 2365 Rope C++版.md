<!--
.. title: POJ 2365 Rope C++版
.. slug: poj-2365
.. date: 2013-04-07T08:59:42+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2365](http://poj.org/problem?id=2365)

题目比较简单给出每个点的坐标，以及每个钉子的半径，求一圈连线的长度，我们知道连线的距离就是没两个点之间的距离相加在加上一个钉子的周长，

不过自己比较傻，先开始r定义成了int，然后一直WA,

代码如下：

	:::cpp
	#include <IOSTREAM>
	#include <CMATH>
	using namespace std;
	#define PI 3.1415926

	double dis(double x1,double x2,double y1, double y2)
	{
		return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
	}
	int main()
	{
		int i,n;
		double x[110],y[110],r,sum=0;
		cin>>n>>r;
		cin>>x[0]>>y[0];
		for (i=1;i<n;i++)
		{
			cin>>x[i]>>y[i];
			sum+=dis(x[i],x[i-1],y[i],y[i-1]);
		}
		sum+=dis(x[n-1],x[0],y[n-1],y[0]);
		sum+=2*PI*r;
		printf("%.2lfn",sum);
	}