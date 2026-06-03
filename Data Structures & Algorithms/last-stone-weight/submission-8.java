
class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq=new PriorityQueue<Integer>(Collections.reverseOrder());
        for(int i:stones){
            pq.add(i);
        }

        while(pq.size()>1){
            int big=pq.poll();
            int small=pq.poll();
            int gap=big-small;
            System.out.println(big);
            if(gap==0){
                continue;
                //pq.add(0);
            }
            else{
                pq.add(gap);
            }
        }
        if(pq.isEmpty()){
            return 0;
        }
        return pq.peek();
    }
}
