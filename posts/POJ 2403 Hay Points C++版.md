<!--
.. title: POJ 2403 Hay Points C++版
.. slug: poj-2403
.. date: 2013-04-07T09:52:40+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1627](http://poj.org/problem?id=1627)


字符串暴力匹配，根据题意，我们为每个单词加上权，然后输出后面给出的一句话的总权值，

没什么解法，利用结构体去保存每个单词和对应的权值，然后依次去匹配就可以了，居然可以0MS，可见他的测试数据一般，不复杂，不然这样的傻办法应该会花很多时间的。
 

	:::cpp
	/*Problem: 2403		User: awq123
	**Memory: 252K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>

	using namespace std;

	struct NODE
	{
	    char str[20];
	    long int num;
	}node[1005];

	int main()
	{
	    int i,n,m;
	    long int sum;
	    cin>>n>>m;
	    for(i=1;i<=n;i++)
	    {
		cin>>node[i].str>>node[i].num;
	    }
	    while(m--)
	    {
		sum=0;
		char tmp[20];
		while(cin>>tmp)
		{
		    if(tmp[0]=='.')
		    {
		        cout<<sum<<endl;
		        break;
		    }
		    for(i=1;i<=n;i++)
		    {
		        if(strcmp(tmp,node[i].str)==0)
		            sum+=node[i].num;
		    }
		}
	    }

	}