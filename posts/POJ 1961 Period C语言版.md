<!--
.. title: POJ 1961 Period C语言版
.. slug: poj-1961
.. date: 2013-04-07T08:32:25+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1961](http://poj.org/problem?id=1961)

解释下题意，先输入字符串得长度，和字符串，然后输出所有前n位重复得情况例如输入例子  
字符串为aabaabaabaab  
前2位也就是aa是a重复2次  
前6位也就是aabaab是aab重复2次  
前9位也就是aabaabaab是aab重复3次  
前12位也就是aabaabaabaab是aab重复4次  

利用KMP算法，匹配最长重复子串，然后针对每个长度找出符合条件得情况


代码如下：

	:::cpp
	/*Problem: 1961		User: awq123
	**Memory: 5064K		Time: 172MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	using namespace std;

	int main()
	{
		int i,j,t,len,next[1000005];
		char str[1000005];
		t=1;
		while(scanf("%d",&len;)&&len;)
		{
			scanf("%s",str);
			next[0]=-1;
			i=0;
			j=-1;
			while(str[i]!='\00')
			{
				if(j==-1||str[i]==str[j])
				{
					i++;
					j++;
					next[i]=j;
				}
				else
					j=next[j];
			}
			printf("Test case #%dn",t++);
			for(i=2;i<=len;i++)
			{
				j=i-next[i];  //求循环节得长度
				if(i%j==0&&i;!=j)  //长度整除这个子串长度，且不为本身
					printf("%d %dn",i,i/j);
			}
			printf("n");
		}
	}