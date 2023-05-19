import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



class Result {

    /*
     * Complete the 'preprocessDate' function below.
     *
     * The function is expected to return a STRING_ARRAY.
     * The function accepts STRING_ARRAY dates as parameter.
     */

    public static List<String> preprocessDate(List<String> dates) {
        List<String> ans = new ArrayList<>();
        HashMap<String,String> map = new HashMap<>();
        map.put("Jan","01");
        map.put("Feb","02");
        map.put("Mar","03");
        map.put("Apr","04");
        map.put("May","05");
        map.put("Jun","06");
        map.put("Jul","07");
        map.put("Aug","08");
        map.put("Sep","09");
        map.put("Oct","10");
        map.put("Nov","11");
        map.put("Dec","12");
        for(int i=0;i<dates.size();i++)
        {
            ans.add(solve(dates.get(i), map));
        }
        return ans;
    }
    public static String solve(String date, HashMap<String,String> map)
    {
        
        StringBuilder sb = new StringBuilder();
        if(date.length() == 13)
        {
            return sb.append(date.substring(9))
                    .append("-")
                    .append(map.get(date.substring(5,8)))
                    .append("-").append(date.substring(0,2))
                    .toString();
        }
        
        return sb.append(date.substring(8))
                    .append("-")
                    .append(map.get(date.substring(4,7)))
                    .append("-0").append(date.substring(0,1))
                    .toString();
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int datesCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> dates = IntStream.range(0, datesCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .collect(toList());

        List<String> result = Result.preprocessDate(dates);

        bufferedWriter.write(
            result.stream()
                .collect(joining("\n"))
            + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}
