class Solution {
    public void helper(int[] nums, int curr, List<Integer> res, List<List<Integer>> result) {
        result.add(new ArrayList<>(res));
        for (int i = curr; i < nums.length; i++) {
            res.add(nums[i]);            
            helper(nums, i + 1, res, result);
            res.remove(res.size() - 1);   
        }
    }

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        helper(nums, 0, new ArrayList<>(), result);
        return result;
    }
}
