public class Solution {
    public int maxProfit(int[] prices) {
        
        int buy1 = Integer.MAX_VALUE;
        int profit1 = 0;
        
        int buy2 = Integer.MIN_VALUE;
        int sell2  = 0;
        
        for(int i=0; i<prices.length; i++) {
            buy1 = Math.min(buy1, prices[i]);
            profit1 = Math.max(profit1, prices[i] - buy1);
            
            buy2 = Math.max(buy2, profit1 - prices[i]);
            sell2 = Math.max(sell2, prices[i] + buy2);
        }
        
        return sell2;
    }
}