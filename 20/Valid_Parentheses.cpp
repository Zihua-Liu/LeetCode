class Solution {
public:
    bool isValid(string s) {
        stack<char> s1;
        for(int i = 0; i < s.length(); i++)
        {
        	if(s[i] == '(')
        		s1.push('(');
        	if(s[i] == '[')
        		s1.push('[');
        	if(s[i] == '{')
        		s1.push('{');
        	if(s[i] == ')')
        	{
        		if (s1.empty() || s1.top() != '(')
        			return false;
        		s1.pop();
        	}
        	if(s[i] == ']')
        	{
        		if (s1.empty() || s1.top() != '[')
        			return false;
        		s1.pop();
        	}
        	if(s[i] == '}')
        	{
        		if (s1.empty() || s1.top() != '{')
        			return false;
        		s1.pop();
        	}
        }
        if (s1.empty())
        	return true;
        return false;
    }
};