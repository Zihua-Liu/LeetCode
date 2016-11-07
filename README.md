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
