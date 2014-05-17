<!--
.. title: POJ 2305 Basic remains C++版
.. slug: poj-2305
.. date: 2013-04-07T08:55:57+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1088](http://poj.org/problem?id=1088)

解释下题意，给出进制b的两个数p，m问满足p=a*m+k的最小正k值，其实我们变换下就是k=p%m

我的开始的思路就是利用字符串模拟取余的过程，没参考什么算法，写得很笨拙，完全无法模拟高精度的取余

贴下我的超时代码，可能还有问题！

	:::cpp
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		freopen("Input.txt", "r", stdin);
		int i,j,b,lenp,lenm;
		char p[1005],m[1005];
		while (scanf("%d",&b;)&&b;)
		{
			scanf("%s %s",p,m);
			lenp=strlen(p);
			lenm=strlen(m);
			for(i=0;i<lenp/2;i++)
			{
				char temp;
				temp=p[i];
				p[i]=p[lenp-i-1];
				p[lenp-i-1]=temp;
			}
			for(i=0;i<lenm/2;i++)
			{
				char temp;
				temp=m[i];
				m[i]=m[lenm-i-1];
				m[lenm-i-1]=temp;
			}
			while (lenp>=lenm)
			{
				for(i=0;i<lenm;i++)
				{
					j=i;
					if(p[lenp-lenm+i]<m[i])
					{
						p[lenp-lenm+i+1]--;
						while (p[lenp-lenm+j+1]<'0')
						{
							p[lenp-lenm+j+2]--;
							p[lenp-lenm+j+1]+=b;
							j++;
						}
						p[lenp-lenm+i]+=b;
					}
					p[lenp-lenm+i]-=m[i]-'0';
				}
				while (p[lenp-1]=='0')
				{
					lenp--;
				}
				p[lenp]='\00';
			}
			for(i=lenp-1;i>=0;i--)
				printf("%c",p[i]);
			printf("n");
		}
	}


没什么思路，查看了下别人的解题报告有了点思路，发现，我们应该先讲数化为10进制，然后进行取余操作，未为了避免数据太大，当p比m大的时候就取一次余，这样就得到了10进制的余数，然后将其转换为b进制输出就是了！

代码如下：

	:::cpp	
	/*Problem: 2305		User: awq123
	**Memory: 232K		Time: 16MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int i,j,b,lenp,lenm;
		long int pa,mb;
		char p[1005],m[1005];
		while (scanf("%d",&b;)&&b;)
		{
			scanf("%s %s",p,m);
			lenp=strlen(p);
			lenm=strlen(m);
			pa=0;
			mb=0;
			for(i=0;i<lenm;i++)
			{
				mb*=b;
				mb+=m[i]-'0';
			}
			for(i=0;i<lenp;i++)
			{
				pa*=b;
				pa+=p[i]-'0';
				if(pa>=mb)
					pa=pa%mb;
			}
			if(pa==0)
			{
				cout<<0<<endl;
				continue;
			}
			else
			{
				i=0;
				while(pa!=0)
				{
					p[i++]=pa%b+'0';
					pa/=b;
				}
				p[i]='\00';
				lenp=strlen(p);
				for(i=lenp-1;i>=0;i--)
					cout<<p[i];
				cout<<endl;
			}
		}
	}	