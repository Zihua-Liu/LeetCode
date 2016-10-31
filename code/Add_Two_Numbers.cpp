/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution
{
public:
	ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
	{
		int adder1, adder2, sum;
		ListNode* ptr1 = l1;
		ListNode* ptr2 = l2;
		ListNode* result = new ListNode(0);
		ListNode* result_ptr = result;
		while((ptr1 !=  NULL && ptr1->next != NULL) || (ptr2 !=  NULL && ptr2->next != NULL) )
		{
			if (ptr1 != NULL)
				adder1 = ptr1->val;
			else
				adder1 = 0;
			
			if (ptr2 != NULL)
				adder2 = ptr2->val;
			else
				adder2 = 0;

			sum = adder1 + adder2 + result_ptr->val;
			result_ptr->val = sum % 10;
			result_ptr->next = new ListNode(sum / 10);
			if (ptr1 != NULL)
				ptr1 = ptr1->next;
			if (ptr2 != NULL)
				ptr2 = ptr2->next;
			result_ptr = result_ptr->next;
		}

		if (ptr1 != NULL)
			adder1 = ptr1->val;
		else
			adder1 = 0;
			
		if (ptr2 != NULL)
			adder2 = ptr2->val;
		else
			adder2 = 0;

		sum = adder1 + adder2 + result_ptr->val;
		result_ptr->val = sum % 10;
		if (sum > 9)
			result_ptr->next = new ListNode(sum / 10);
		return result;
	}
};