class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
    	if (head->next == NULL)
    		return NULL;
        stack<ListNode*> s;
        ListNode* ptr = head;
        while(ptr != NULL)
        {
        	s.push(ptr);
        	ptr = ptr->next;
        }
        for(int i = 0; i < n; i++)
        {
        	ptr = s.top();
        	s.pop();
        }
        if (ptr == head)
        	head = ptr->next;
        delete ptr;
        if (!s.empty())
        	ptr = s.top();
        if (ptr->next != NULL)
        	ptr->next = ptr->next->next;
        return head;
    }
};