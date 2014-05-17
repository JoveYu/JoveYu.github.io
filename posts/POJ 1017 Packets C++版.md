<!--
.. title: POJ 1017 Packets C++版
.. slug: poj-1017
.. date: 2013-04-07T04:21:51+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1017](http://poj.org/problem?id=1017)

这个题要求我们给1×1 2×2 3×3 4×4 5×5 6×6 六种包裹打包用最少的包裹，一个平面问题，我画图做的，在图中看比自己想快多了，后面会附加我做题的图，代码启发自某博客，加以研究。
装3×3时有其中可插入的2×2如图，1个3×3的，有5个2×2，其他的依次类推,
2个3×3可以放3个2×2,
3个3×3可以放1个2×2,
这样剩下的就是1×1的了
当然我门应该注意如果2×2或1×1多于间隙就要单独开箱来装了

代码如下

	:::cpp
	/*Problem: 1017		User: awq123
	**Memory: 172K		Time: 16MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include<stdio.h>
	/*在linux下编译g++的iostream没有老式的输出*/
	using namespace std;

	int cc[4] = {0, 5, 3, 1};
	/*装有3*3 的箱子可放2*2的包数 当放1个3*3可以放5个2*2 2个可放3个2*2*/
	int a, b, c, d, e, f;
	int num;

	int main()
	{
		while (scanf("%d%d%d%d%d%d", &a, &b, &c, &d, &e;, &f))
		{
			if (a==0 && b==0 && c==0 && d==0 && e==0 && f==0) break; 
				/* 4*4，5*5,6*6 的无疑每个都需要一个盒子 */
				num = d + e + f + (c+3)/4;/* (c+3)/4 是对于 3*3 的包需要的 6*6 大小的盒子数 */
			int aa, bb;
			bb = 5*d + cc[c%4];
			/* bb 是已有的包里能放多少个2*2的，每个放 4*4 的盒子还可以放 5 个 2*2的 */
			if (b > bb) 
				num += (b-bb+8)/9;
				/* 如果可装2*2的个数小于2*2的总个数新开箱子 每1～9 个开一个新箱子  */
			aa = num*36 - f*36 - e*25 - d*16 - c*9 - b*4;
			/* 总共剩下可以装1*1箱子的个数 */
			if (a>aa) 
				num += (a-aa+35)/36;
				/* 如果可装1*1的个数小于1*1的总个数新开箱子 每1～36开一个新箱子 */
			printf("%dn", num);
		}
	return 0;
	}