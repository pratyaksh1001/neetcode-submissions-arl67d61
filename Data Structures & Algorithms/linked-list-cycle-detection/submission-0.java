/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */


class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> s=new HashSet<ListNode>();
        while(head!=null){
            if(s.contains(head)){
                return true;
            }
            s.add(head);
            head=head.next;
        }
        return false;
    }
}
