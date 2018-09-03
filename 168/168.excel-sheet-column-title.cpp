/*
 * [168] Excel Sheet Column Title
 *
 * https://leetcode.com/problems/excel-sheet-column-title/description/
 *
 * algorithms
 * Easy (27.87%)
 * Total Accepted:    147.5K
 * Total Submissions: 529.3K
 * Testcase Example:  '1'
 *
 * Given a positive integer, return its corresponding column title as appear in
 * an Excel sheet.
 * 
 * For example:
 * 
 * 
 * ⁠   1 -> A
 * ⁠   2 -> B
 * ⁠   3 -> C
 * ⁠   ...
 * ⁠   26 -> Z
 * ⁠   27 -> AA
 * ⁠   28 -> AB 
 * ⁠   ...
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: 1
 * Output: "A"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 28
 * Output: "AB"
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: 701
 * Output: "ZY"
 * 
 * 
 */
#include <iostream>
#include<string>
using namespace std;

class Solution {
public:
    string convertToTitle(int n) {
        string ans = "";
        while (n > 0)
        {
        	n = n - 1;
        	char current_letter[] = "A";
        	current_letter[0] += (int)n % 26;
        	ans = current_letter + ans;
        	n = n / 26;
        }
        return ans;
    }
};

