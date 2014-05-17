<!--
.. title: POJ 1013 Counterfeit Dollar C++版
.. slug: poj-1013
.. date: 2013-04-07T06:20:11+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1013](http://poj.org/problem?id=1013)


解释下题意，有12个硬币，有一个是假的跟其他重量不一样，要求你通过三次称量找出这个硬币！称量不用你考虑，题目说了三次称量一定能找到这个硬币，我们所做的就是分析数据！

我们来讲解下称量：
even则盘两边的必然都是真的
up左盘有轻假硬币或者右盘有重假硬币
down右盘有轻假硬币或者左盘有重假硬币

其中有点需要特别说明，也是解题的要点，就是up和down的情况下没有称的一定是真的！没有这个判断是完成不了题目的！

这道题花了我大概3个小时，百思不得其解，一直我定义的cmp都是4个字节，觉得也没问题，但是最后改成5就AC了，我擦，当时就想骂人了，原来忘记了，一个字符串需要'\00'做结尾，我是说怎么数据都对还能错的，还是自己大意了！

具体的思路看注释吧

代码如下：

	:::cpp
	/*Problem: 1013		User: awq123
	**Memory: 176K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int i,j,len,n,d[12],temp[12];
		char left[12],right[12],cmp[5];
		scanf("%d",&n;);
		while(n--)
		{
			//d数组表示真假性-1表示可能假0不知道1真2可能真
			memset(d,0,sizeof(d));
			for(i=0;i<3;i++)
			{
				scanf("%s%s%s",left,right,cmp);
				len=strlen(left);
				if(cmp[0]=='e')//even
				{
					for(j=0;j<len;j++)
					{
						d[left[j]-'A']=1;
						d[right[j]-'A']=1;
						//标记真的
					}
				}
				else if(cmp[0]=='u')//up
				{
					memset(temp,0,sizeof(temp));
					for(j=0;j<len;j++)
					{
						if(d[left[j]-'A']==-1)
							d[left[j]-'A']=1;
						//若既可能真，也可能假，则为真
						else if(d[left[j]-'A']==0)
							d[left[j]-'A']=2;
						//否则将不知道的标记为可能真
						//下面的不一一列举
						if(d[right[j]-'A']==2)
							d[right[j]-'A']=1;
						else if(d[right[j]-'A']==0)
							d[right[j]-'A']=-1;
						temp[left[j]-'A']=1;
						temp[right[j]-'A']=1;
						//标记这次比较用过的数
					}
					for(j=0;j<12;j++)
						if(temp[j]==0)
							d[j]=1;
					//给没用过的数标记成真
				}
				else if(cmp[0]=='d')//down
				{
					memset(temp,0,sizeof(temp));
					for(j=0;j<len;j++)
					{
						if(d[left[j]-'A']==2)
							d[left[j]-'A']=1;
						else if(d[left[j]-'A']==0)
							d[left[j]-'A']=-1;
						if(d[right[j]-'A']==-1)
							d[right[j]-'A']=1;
						else if(d[right[j]-'A']==0)
							d[right[j]-'A']=2;
						temp[left[j]-'A']=1;
						temp[right[j]-'A']=1;
					}
					for(j=0;j<12;j++)
						if(temp[j]==0)
							d[j]=1;
				}
			}
			for(i=0;i<12;i++)//扫描输出结果
			{
				if(d[i]==-1)
					printf("%c is the counterfeit coin and it is light.n",i+'A');
				if(d[i]==2)
					printf("%c is the counterfeit coin and it is heavy.n",i+'A');
			}	
		}
	}
