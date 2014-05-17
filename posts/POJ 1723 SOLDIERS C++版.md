<!--
.. title: POJ 1723 SOLDIERS C++版
.. slug: poj-1723
.. date: 2013-04-07T05:00:14+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：<a href="http://poj.org/problem?id=1723">http://poj.org/problem?id=1723</a>

题目给出很多士兵的坐标，求把这些士兵移动到一条线上的最小步数，这年头没google翻译还是很难看懂题目，那些ACM大神一定英语很好，其实把，我的提升空间还是很大的，嘻嘻！！

其中利用了<algorithm>的sort函数大大节约了排序的时间！

解释下算法，转换成y坐标相同的排序，分开x和y坐标处理。

对y坐标排序之后就可以轻松求出中位数，进而计算出移动步数。

麻烦一点的是x坐标。首先我们对输入的点按照x坐标递增排序。排序后所有点的相对位置和最终要求的排列的相对位置是一致的。 如果排序后点p在q左边，而最终的排列q在p左边，那么可以通过交换两者的位置，一个步数增加，一个步数减少，总和是不变的。

我们现在的任务是，找出一个标准点，让所有点从这条左边线开始依次排列。由于排序后的点相对位置和最终是一致的，我们按照排序后的下标依次x[i]-=i，得到的点被横向移动后，应该聚集到那标准点上下，而这个移动过程应该消耗最少的步数！
代码如下：

	:::cpp
	/*Problem: 1723		User: awq123
	**Memory: 332K		Time: 94MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <algorithm>
	using namespace std;
	 
	int main()
	{
		int n,x[10001],y[10001];
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>x[i]>>y[i];
		sort(x,x+n);
		sort(y,y+n);
		for (int i=0;i<n;i++)
			x[i]-=i;
		sort(x,x+n);
		int m =0;
		for (int i=0;i<n/2;i++)
			m+=x[n-1-i]-x[i]+y[n-1-i]-y[i];
		cout<<m<<endl;
	}
