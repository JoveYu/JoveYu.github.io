<!--
.. title: POJ 2309 BST C++版
.. slug: poj-2309
.. date: 2013-04-07T05:43:35+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2309](http://poj.org/problem?id=2309)


标准二叉生成树，输入一个数，求以这个数为根的最边上两个数；上图



我们来看图分析，这是个标准BST图，简单分析下，我们可以轻松的看出所有的奇数都在第一行，这点由利于提升算法的速度省去一些时间，主要来看每个节点，因为每个节点都有两个分叉，那么这个数因式分解后有几个2这个数就再第几行，然后看一个节点的数等于两边最远的两个数和的一半，还有同一行的数，与最远数的差距，同最左边的一样，比如题目中的10离9差1，其实同一行最左边的2离1也差1，通过最左行纯幂次，我们可以看出，其中这个差和幂次的关系，这样就能算出每一个的答案了。思路不难，主要是画图看。

代码如下：

	:::cpp
	/*Problem: 2309		User: awq123
	**Memory: 252K		Time: 16MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cmath>
	using namespace std;

	int main()
	{
		long long int t,m,n;
		int count;
		cin>>t;
		while(t--)
		{
			cin>>m;
			n=m;
			count=0;
			while(n%2==0)
			{
				n/=2;
				count++;
			}
			if(count==0)
				cout<<m<<" "<<m<<endl;
			else
				cout<<m-(long long int)pow(2.0,count)+1<<" "<<m+(long long int)pow(2.0,count)-1<<endl;
			
		}
	}

还有一种利用位运算的，我不懂，没办法，代码贴出来看看：

	:::cpp
	#include <cstdio>
	#include <math.h>
	using namespace std;
	int main(){
		int nCase;
		scanf("%d",&nCase;);
		while(nCase--){
			int n;
			scanf("%d",&n;);
			int k=n&(-n);
			k--;
			printf("%d %dn",n-k,n+k);	
		}
		return 0;
	} 
