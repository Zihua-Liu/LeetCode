/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    	if (l1 == NULL)
    		return l2;
        ListNode* ptr_1 = l1;
        ListNode* ptr_2 = l2;
        ListNode* result = new ListNode(0);
        ListNode* tmp = result;
        while(ptr_1 != NULL && ptr_2 != NULL)
        {
        	if(ptr_1->val < ptr_2->val)
        	{
        		tmp->val = ptr_1->val;
        		ptr_1 = ptr_1->next;
        	}
        	else
        	{
        		tmp->val = ptr_2->val;
        		ptr_2 = ptr_2->next;
        	}
        	tmp->next = new ListNode(0);
        	tmp = tmp->next;
        }
        if (ptr_1 == NULL)
        {
        	while(ptr_2->next != NULL)
        	{
        		tmp->val = ptr_2->val;
        		ptr_2 = ptr_2->next;
        		tmp->next = new ListNode(0);
        		tmp = tmp->next;
        	}
        	tmp->val = ptr_2->val;
        }
        if (ptr_2 == NULL)
        {
        	while(ptr_1->next != NULL)
        	{
        		tmp->val = ptr_1->val;
        		ptr_1 = ptr_1->next;
        		tmp->next = new ListNode(0);
        		tmp = tmp->next;
        	}
        	tmp->val = ptr_1->val;
        }
        return result;
    }
};