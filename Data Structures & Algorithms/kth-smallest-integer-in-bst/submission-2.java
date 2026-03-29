/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public ArrayList<Integer> r=new ArrayList<>();

    public void helper(TreeNode root,int k){
        if(root==null || r.size()==k){
            return;
        }
        helper(root.left,k);
        this.r.add(root.val);
        helper(root.right,k);
    }

    public int kthSmallest(TreeNode root, int k) {
        this.helper(root,k);
        System.out.println(r);
        return this.r.get(k-1);
    }
}
