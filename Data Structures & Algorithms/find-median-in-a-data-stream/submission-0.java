class MedianFinder {
    PriorityQueue<Integer> maxHeap; // left side (smaller half)
    PriorityQueue<Integer> minHeap; // right side (larger half)

    public MedianFinder() {
        maxHeap = new PriorityQueue<>(Comparator.reverseOrder()); // Max Heap
        minHeap = new PriorityQueue<>(); // Min Heap
    }
    
    public void addNum(int num) {
        // Step 1: Add number
        if (maxHeap.isEmpty() || num <= maxHeap.peek()) {
            maxHeap.add(num);
        } else {
            minHeap.add(num);
        }

        // Step 2: Rebalance
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.add(maxHeap.poll());
        } else if (minHeap.size() > maxHeap.size() + 1) {
            maxHeap.add(minHeap.poll());
        }
    }
    
    public double findMedian() {
        if (maxHeap.size() == minHeap.size()) {
            return (maxHeap.peek() + minHeap.peek()) / 2.0;
        } 
        else if (maxHeap.size() > minHeap.size()) {
            return maxHeap.peek();
        } 
        else {
            return minHeap.peek();
        }
    }
}