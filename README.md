Work list(争取每天做一道。。)
===================

1.Two Sum --------C<br /><br />
2.Add_TWO_Numbers--------C++<br /><br />
3.Longest Substring Without Repeating Characters--------C++<br />
&nbsp;&nbsp;&nbsp;&nbsp;worst time complexity is O(n^2)<br />
&nbsp;&nbsp;&nbsp;&nbsp;space complexity is O(number_of(character))<br />
&nbsp;&nbsp;&nbsp;&nbsp;maybe could optimized by using KMP<br /><br />
4.Median of Two Sorted Arrays--------?<br />
&nbsp;&nbsp;&nbsp;&nbsp;Cannot solve yet!<br /><br />
5.Longest Palindromic Substring--------C++<br />
&nbsp;&nbsp;&nbsp;&nbsp;利用动态规划算法降低复杂度<br /><br />
6.ZigZag Conversion--------C++<br />
&nbsp;&nbsp;&nbsp;&nbsp;注意当rowNums=1，这种特殊情况，需要在while循环最后加入判断<br /><br />
7.Reverse_Integer--------C++<br />
&nbsp;&nbsp;&nbsp;&nbsp;reverse之后的数可能超过整形表示范围，注意特殊处理，应该返回0。<br /><br />
8.String to Integer--------C++<br />
&nbsp;&nbsp;&nbsp;&nbsp;没啥技术含量，关键在于各种case的边界条件的处理。<br /><br />
9.Palindrome Number--------C++<br />
&nbsp;&nbsp;&nbsp;&nbsp;一开始想用递归做，然而发现无法处理子串开头是0的情况<br />
&nbsp;&nbsp;&nbsp;&nbsp;后来老老实实用了一个循环，然而用了两个局部变量，也不知道算不算使用了额外的空间。。。<br /><br />
10.Regular Express Matching--------python<br />
&nbsp;&nbsp;&nbsp;&nbsp;用递归还比较容易，不断根据各种匹配模式比较字串即可<br />
&nbsp;&nbsp;&nbsp;&nbsp;在递归函数第一步先比较最后一个字符是为了剪枝，要不然会超时<br /><br />
11.Container with most water--------python<br />
&nbsp;&nbsp;&nbsp;&nbsp;用暴力解法，时间复杂度是O(n^2)的<br />
&nbsp;&nbsp;&nbsp;&nbsp;注意一条性质，当取得最大容器时，容器左侧不可能再有比容器左边沿更高的边，右边同样不可能存在比右边沿更高的边。所以初始时取最两边的边最为边沿，不断向中间靠拢，并更新容积的最大值即可。<br /><br />
12.Integer to Roman--------python<br />
&nbsp;&nbsp;&nbsp;&nbsp;纯暴力。。<br /><br />
13.Roman to Integer--------C++<br />
&nbsp;&nbsp;&nbsp;&nbsp;没啥技术含量，直到罗马数字怎么转成十进制数就行了。<br /><br />
14.Longest Common Prefix--------python<br />
&nbsp;&nbsp;&nbsp;&nbsp;复杂度比较高，依次比较每个字符串对应的位置。如果相同就把公共串的h长度加1。不知道有木有优化算法。<br /><br />
15.3Sum--------python<br />
&nbsp;&nbsp;&nbsp;&nbsp;大致方法是对数组排序，然后固定两个数，用二分法找第三个数。由于数组有序，注意各种剪枝<br />
&nbsp;&nbsp;&nbsp;&nbsp;比较重要的一个剪枝是如果期望的结果已经在结果集中了，直接剪枝，不要二分法再去找第三个数了。之前一直超时就是没有注意这里。。<br /><br />
16.3Sum Closest--------python<br />
&nbsp;&nbsp;&nbsp;&nbsp;对数组排序，扫描第一个数，第二个数从第一个数后面的子数组第一个元素开始，第三个数从子数组的最后一个元素开始<br />
&nbsp;&nbsp;&nbsp;&nbsp;复杂度是O(n^2)的<br /><br />
16.Letter Combinations of a Phone Number--------python<br />
&nbsp;&nbsp;&nbsp;&nbsp;先算出总的答案数量，然后根据答案编号做除法以及余数运算去寻找对应的字符串<br /><br />
