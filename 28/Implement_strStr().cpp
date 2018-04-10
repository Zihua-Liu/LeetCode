class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.length() == 0)
            return 0;
        return KMPStrMatching(haystack, needle, findNext(needle));
    }

    int* findNext(string p)
    {
    	int i = 0;
    	int k = -1;
    	int m = p.length();
    	int *next = new int[m];
    	next[0] = -1;
    	while(i < m)
    	{
    		while(k >= 0 && p[i] != p[k])
    			k = next[k];
    		i++;
    		k++;
    		if (i == m)
    			break;
    		if (p[i] == p[k])
    			next[i] = next[k];
    		else
    			next[i] = k;
    	}
    	return next;
    }

    int KMPStrMatching(string T, string P, int * N)
    {
    	int i = 0; int j = 0;
    	int plen = P.length();
    	int tlen = T.length();
    	if(tlen < plen)
    		return -1;
    	while(i < plen && j < tlen)
    	{
    		if (i == -1 || T[j] == P[i])
    			i++, j++;
    		else
    			i = N[i];
    	}
    	if (i >= plen)
    		return (j - plen);
    	else
    		return -1;
    }
};