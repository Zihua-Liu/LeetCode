/*
 * [127] Word Ladder
 *
 * https://leetcode.com/problems/word-ladder/description/
 *
 * algorithms
 * Medium (20.47%)
 * Total Accepted:    172.9K
 * Total Submissions: 844.8K
 * Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
 *
 * Given two words (beginWord and endWord), and a dictionary's word list, find
 * the length of shortest transformation sequence from beginWord to endWord,
 * such that:
 * 
 * 
 * Only one letter can be changed at a time.
 * Each transformed word must exist in the word list. Note that beginWord is
 * not a transformed word.
 * 
 * 
 * Note:
 * 
 * 
 * Return 0 if there is no such transformation sequence.
 * All words have the same length.
 * All words contain only lowercase alphabetic characters.
 * You may assume no duplicates in the word list.
 * You may assume beginWord and endWord are non-empty and are not the same.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input:
 * beginWord = "hit",
 * endWord = "cog",
 * wordList = ["hot","dot","dog","lot","log","cog"]
 * 
 * Output: 5
 * 
 * Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
 * "dog" -> "cog",
 * return its length 5.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input:
 * beginWord = "hit"
 * endWord = "cog"
 * wordList = ["hot","dot","dog","lot","log"]
 * 
 * Output: 0
 * 
 * Explanation: The endWord "cog" is not in wordList, therefore no possible
 * transformation.
 * 
 * 
 * 
 * 
 * 
 */
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_map<string, int> used_word;
        queue<string> que;
        que.push(beginWord);
        used_word[beginWord] = 1;
        while (!que.empty())
        {
        	string top = que.front();
        	que.pop();
        	if (top == endWord)
        		return used_word[top];
        	for (auto &word: wordList)
        	{
        		if (validTransform(top, word) && !used_word[word])
        		{	
        			used_word[word] = used_word[top] + 1;
        			que.push(word);
        		}
        	}
        }
        return 0;
    }

    bool validTransform(string source, string target)
    {
    	if (source.size() != target.size())
    		return false;
    	int diff = 0;
    	for (int i = 0; i < source.size(); i++)
    	{
    		diff += source[i] != target[i];
    	}
    	return diff == 1;
    }
};
