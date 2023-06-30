package practiceProblems;
class Solution {
    public String reorganizeString(String s) {
        Map<Character, Integer> m = new HashMap<Character, Integer>();
        char [] strArr = s.toCharArray();
        for (char c: strArr) {
            m.put(c, m.getOrDefault(c, 0) + 1);
        }
        System.out.println(m);
        PriorityQueue<Character> pq = new PriorityQueue<Character>((a,b) -> (m.get(b) - m.get(a)));
        for (char k : m.keySet()){
            pq.offer(k);
        }
        System.out.println(pq);
        String res = "";
        char cached = 0;
        while(!pq.isEmpty()){
            char c = pq.poll();
            int freq = m.get(c) - 1;

            m.put(c, freq);
            res += c;
            if (cached != 0) {
                pq.offer(cached);
            }
            if (freq > 0) {
                cached = c;
            } else {
                cached = 0;
            }
        }
        if(cached != 0) {
            return "";
        }
        return res;
    }
}