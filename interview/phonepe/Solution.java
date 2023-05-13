import java.io.*;
import java.util.*;
import java.util.Collection;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.core.JsonProcessingException;

// Main class should be named 'Solution'
class Solution {
    private static Map<Integer, ArrayList<String>> startTrack = new HashMap<>();

    public static void main(String[] args) {
        
        
        ArrayList<String> tags1 = new ArrayList<>(Arrays.asList("UPI", "Karnataka", "Bangalore"));;
        
        
        startTracking(1112,new ArrayList<>(Arrays.asList("UPI", "Karnataka", "Bangalore")));
        startTracking(2451,new ArrayList<>(Arrays.asList("UPI", "Karnataka", "Mysore")));
        startTracking(3421,new ArrayList<>(Arrays.asList("UPI", "Rajasthan", "Jaipur")));
        startTracking(1221,new ArrayList<>(Arrays.asList("Wallet", "Karnataka", "Bangalore")));
        
        System.out.println(getCounts(new ArrayList<>(Arrays.asList("UPI"))));
        System.out.println(getCounts(new ArrayList<>(Arrays.asList("UPI", "Karnataka"))));
        System.out.println(getCounts(new ArrayList<>(Arrays.asList("UPI", "Karnataka", "Bangalore"))));
        System.out.println(getCounts(new ArrayList<>(Arrays.asList("Bangalore"))));  
        startTracking(4221,new ArrayList<>(Arrays.asList("Wallet", "Karnataka", "Bangalore")));
        stopTracking(1112); 
        stopTracking(2451);
        System.out.println(getCounts(new ArrayList<>(Arrays.asList("UPI"))));
        System.out.println(getCounts(new ArrayList<>(Arrays.asList("Wallet"))));
        System.out.println(getCounts(new ArrayList<>(Arrays.asList("UPI", "Karnataka", "Bangalore"))));
        
    }
    
    public static Map<Integer, ArrayList<String>> startTracking(Integer id, ArrayList<String> tags){
        
        if(startTrack.get(id) == null){
            ArrayList<String> idTags = new ArrayList<>(tags);
            startTrack.put(id, idTags);
        }
        
        return startTrack;
    }
    
    public static Map<Integer, ArrayList<String>> stopTracking(Integer id){
        
        if(startTrack.get(id) == null){
            System.out.println("id doesn't exist'");
        }else{
            startTrack.remove(id);
        }
        
        return startTrack;
    } 
    
    public static int getCounts(ArrayList<String> checkTags){
        int count =0;
        for(Map.Entry<Integer, ArrayList<String>> tag: startTrack.entrySet()){
            ArrayList<String> tagList = tag.getValue();
            if(matchTags(tagList,checkTags)){
                count++;
            }
        }
                return count;

    }
    
    public static Boolean matchTags(ArrayList<String> tagList,ArrayList<String> checkTags){
        int i=0;
        while(tagList.size() > i && checkTags.size()>i){
            if(!tagList.get(i).equals(checkTags.get(i))){
                return false;
            }
            i++;
        }
        
        return true;
    }
    
}