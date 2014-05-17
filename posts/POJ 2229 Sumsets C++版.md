<!--
.. title: POJ 2229 Sumsets C++版
.. slug: poj-2229
.. date: 2013-04-07T05:33:38+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2229](http://poj.org/problem?id=2229)


这个题意简单，我没看翻译都看懂了，哈哈，玩笑而已，英语还要提高！

题目要求给出一个数分解成由2的幂次相加的形式，问由多少种分解方式。

我们来分析下，n=1和n=2是很容易判断，为1和2。

n为基数的时候，相当于把n-1的排列每个都加上1，n为偶数的时候，可以看成两种形式，也就是n-2的排列加上两个1，或者所有的数都是偶数的情况，这种情况的数目既n/2的数目。

其实很明显的递归调用，我现开始就是用递归做的，但是递归就是所花费的时间太多，结果超时了，代码如下：

	:::cpp
	#include <cstdio>
	#include <iostream>
	#include <cstring>
	#include <algorithm>
	#include <cmath>
	using namespace std;
	int dj(int n)
	{
		if(n==1||n==2)
			return n;
		else if(n%2==1)
			return dj(n-1);
		else
			return dj(n-2)+dj(n/2);
	}

	int main()
	{
		//freopen("input.txt", "r", stdin); 
		int n;
		cin>>n;
		cout<<dj(n);
	
	}


改用数组储存数据，由小到大依次计算，这样省去的很多重复的运算，我把这称为反递归运算，也就是从递归最深层开始向外算，

不过还是WA了几次，因为output种的这样一句话

>Due to the potential huge size of this number, print only last 9 digits (in base 10 representation).

自然数据会大于这个数，不过我认为int的情况也可能由问题，不过果料儿也就没多想，数据比较好把！

最终代码如下：

	:::cpp
	/*Problem: 2229		User: awq123
	**Memory: 4176K		Time: 172MS
	**Language: C++		Result: Accepted
	*/
	#include <cstdio>
	#include <iostream>
	#include <cstring>
	#include <algorithm>
	#include <cmath>
	using namespace std;

	int main()
	{
		//freopen("input.txt", "r", stdin); 
		int n,a[1000001];
		for(n=1;n<=1000000;n++)
		{
			if(n==1||n==2)
				a[n]=n;
			else if(n%2==1)
				a[n]=a[n-1];
			else
				a[n]=a[n-2]+a[n/2];
			if(a[n]>=1000000000)
				a[n]%=1000000000;
		}
		cin>>n;
		cout<<a[n]<<endl;
	}
