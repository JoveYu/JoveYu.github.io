<!--
.. title: POJ 1042 Gone Fishing C++版
.. slug: poj-1042
.. date: 2013-04-07T08:58:21+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1042](http://poj.org/problem?id=1042)


这题是《算法艺术与信息学竞赛》p13的例题，也算是我学习贪心法的入门把，

解释下题意，有n个湖，给出钓鱼时间，每个湖的钓鱼量，以及每个湖钓一次后的钓鱼量的减少量，一个从第一个湖开始每两个之间的行走时间，我们以第一个例子来看，

>2   
>1   
>10 1   
>2 5   
>2  
 
意思是（一次就是5分钟）

>有2个湖  
>钓鱼1小时  
>每次钓鱼量分别是10，1  
>掉一次后下次的钓鱼量减少2，5  
>从第一个湖到第二个湖要2次的时间  


利用贪心的做法解题，假设在i出停止钓鱼，我们事先把行走的时间减去，就可以认为他在湖之间的移动是瞬间的，然后每次取钓鱼量最大的湖掉一次，直到时间钓完，没有鱼就在第一个点蹲着！

写这个题没有点麻烦，一开始没想到有这么多数组，到用的时候才定义，名字有点乱，一开始超时，后来加了一个符号解决了：


>while(th>0)   //原来是(th)


代码如下，有简单的注释：

	:::cpp
	/*Problem: 1042		User: awq123
	**Memory: 164K		Time: 47MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int max,time[26],i,j,f[26],fb[26],d[26],t[26],n,h;
		while(scanf("%d",&n;)&&n;)
		{
			memset(time,0,sizeof(time));
			max=-1;
			//依次输入数据
			scanf("%d",&h;);
			h*=60;
			for(i=1;i<=n;i++)
				scanf("%d",&fb;[i]);
			for(i=1;i<=n;i++)
				scanf("%d",&d;[i]);
			t[1]=0;
			//这里我们记录的是一共走的时间
			for(i=2;i<=n;i++)
			{
				int temp;
				scanf("%d",&temp;);
				t[i]=t[i-1]+temp;
			}
			//分别计算在每个湖停止的最好情况
			for(i=1;i<=n;i++)
			{
				memcpy(f,fb,(i+1)*sizeof(f[0]));
				int sum=0;
				//减去走的时间
				int th=h-t[i]*5;
				int temp[26];
				memset(temp,0,sizeof(temp));
				//直到把时间取完
				while(th>0)
				{
					int maxn=0,maxi=1;
					//选取最大的一个湖
					for(j=1;j<=i;j++)
						if(f[j]>maxn)
						{
							maxn=f[j];
							maxi=j;
						}
					//运算数据
					temp[maxi]+=5;
					sum+=maxn;
					f[maxi]-=d[maxi];
					th-=5;
				}
				//比较是否为最好情况
				if(sum>max)
				{
					max=sum;
					memcpy(time,temp,(i+1)*sizeof(f[0]));
				}
			}
			//输出
			for(i=1;i<n;i++)
				printf("%d, ",time[i]);
			printf("%dn",time[n]);
			printf("Number of fish expected: %dnn",max);
		}
	}