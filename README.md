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
17.Letter Combinations of a Phone Number--------python<br />
&nbsp;&nbsp;&nbsp;&nbsp;先算出总的答案数量，然后根据答案编号做除法以及余数运算去寻找对应的字符串<br /><br />
18.4 Sum--------python<br />
&nbsp;&nbsp;&nbsp;&nbsp;采用和3 Sum Closest相似的方法，复杂度是O(n^3)<br /><br />
19.Remove Nth Node From End of List--------C++<br/>
&nbsp;&nbsp;&nbsp;&nbsp;用一个栈来实现，注意删除结点位于链表头这种特殊情况<br /><br />
20Valid Parentheses--------C++<br/>
&nbsp;&nbsp;&nbsp;&nbsp;用一个栈来实现<br/><br/>
21.Merge Two Sorted Lists--------C++<br/>
&nbsp;&nbsp;&nbsp;&nbsp;每个链表搞一个指针，一起遍历即可<br/><br/>
22.Generate Parentheses--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;递归实现<br/><br/>
24.Swap Nodes in Pairs--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;注意边界<br/><br/>
26.Remove Duplicates from Sorted Array--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;注意审题，只需改变nums数组前半部分的内容即可<br/><br/>
27.Remove Element--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;首先把要删除的元素用特殊值标记，然后再将数组多余长度中不应删除的元素填入特殊标记的位置即可。<br/><br/>
28.Implement strStr()--------C++<br/>
&nbsp;&nbsp;&nbsp;&nbsp;重点！！！！！应用KMP算法来加快匹配速度！！！KMP算法要掌握！！！可以看一看实现代码。<br/><br/>
29.Divide Two Integers-------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;用除数的移位运算去接近被除数，从被除数中减去除数，同时商上不断累积2的若干次幂<br/><br/>
31.Next Permutation--------C++<br/>
&nbsp;&nbsp;&nbsp;&nbsp;先找到序列中被交换后使得序列增加最小的升序对，然后再将升序对后面的子数组通过排序算法转换为升序排列即可。<br/><br/>
34.Search for a Range--------C++<br/>
&nbsp;&nbsp;&nbsp;&nbsp;在二分法上做做文章即可<br/><br/>
35.Search Insert Position-------C++<br/>
&nbsp;&nbsp;&nbsp;&nbsp;二分法查找即可<br/><br/>
36.Valid Sudoku--------C<br/>
&nbsp;&nbsp;&nbsp;&nbsp;逐行逐列每个子棋盘判断即可<br/><br/>
37.Sudoku Solver--------C<br/>
&nbsp;&nbsp;&nbsp;&nbsp;递归+回溯<br/><br/>
38.Count and Say--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;简单的递归<br/><br/>
39.Combination Sum--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;递归<br/><br/>
40.Combination Sum2--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;对39的代码稍作修改即可<br/><br/>
41.First Missing Positive--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;思路：交换数组元素，使得数组中第i位存放数值(i+1)。最后遍历数组，寻找第一个不符合此要求的元素，返回其下标。整个过程需要遍历两次数组，复杂度为O(n)。<br/><br/>
42.Trapping Rain Water--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;循环往前算，在每个位置看能存储多少水即可。<br/><br/>
43.Multiply Strings--------C++<br/>
&nbsp;&nbsp;&nbsp;&nbsp;大整数乘法，注意在乘法进位以及加法进位的时候要先除以十进位，再在本位取余数<br/><br/>
45.Jump Game II--------C++<br/>
&nbsp;&nbsp;&nbsp;&nbsp;ret:目前为止的jump数<br/>
&nbsp;&nbsp;&nbsp;&nbsp;curRch:从A[0]进行ret次jump之后达到的最大范围<br/>
&nbsp;&nbsp;&nbsp;&nbsp;curMax:从0~i这i+1个A元素中能达到的最大范围<br/>
&nbsp;&nbsp;&nbsp;&nbsp;当curRch < i，说明ret次jump已经不足以覆盖当前第i个元素，因此需要增加一次jump，使之达到记录的curMax。<br/><br/>
46.Permutations--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;简单的递归就可以搞定<br/><br/>
47.Permutations II--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;在46的基础上对递归进行一定的优化，首先先把数组排序，对于重复的元素如果在同一层中已经使用过了就不要再选择这个元素进入下一层递归了<br/><br/>
48.Image Rotation--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;从外到里一圈一圈的旋转90度<br/><br/>
49.Group Anagrams--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;用两层循环做会超时，用一层循环，将每个字符串按字典序重新排序后，将排序后相同的字符串加入字典中同一key值的列表（相当于哈希的方式实现，不会超时。)<br/><br/>
50.Pow(x, n)--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;将n用2进制表示，然后将底数的2^n次方提前算好，然后再求x的n次方，降低复杂度。<br/><br/>
51.N-Queens--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;递归加回溯，基础题<br/><br/>
52.N-Queens--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;在N皇后问题的代码稍微改改就行了<br/><br/>
53.Spiral Matrix--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;基础题<br/><br/>
54.Maximum Subarray--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;不错的题，动态规划算法。c[i]代表nums[0-i]中必须包含nums[i]的最大子段的和。c[i] = max{c[i - 1]+a[i], a[i]} i = 1, 2, ...n。最后遍历数组c，找到最大值返回即可。<br/><br/>
55.Jump Game--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;动态规划算法。c[i]代表从0 - i位置能到达的最远的位置。c[0]=nums[0]，如果c[i-1] < i，代表无法到达i位置，返回false即可。当可以到达i位置时，c[i] = max(c[i-1], i + nums[i])。<br/><br/>
56.Merge Intervals--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;把interval中元素按照start从小到达排序，遍历，检查相邻两个二元组间是否有重叠部分，有重叠则合并。在数组排序时，需要自己写一下sort函数的比较函数。<br/><br/>
57.Insert Interval--------python<br/>
&nbsp;&nbsp;&nbsp;&nbsp;和56一样。把新的元祖插入数组重复56即可<br/><br/>
