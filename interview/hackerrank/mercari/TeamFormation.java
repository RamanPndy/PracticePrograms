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
     * Complete the 'countTeams' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY rating
     *  2. 2D_INTEGER_ARRAY queries
     */

    public static List<Integer> countTeams(List<Integer> rating, List<List<Integer>> queries) {
    // Write your code here
        List<Integer> ans = new ArrayList<>();
        for(int i=0;i<queries.size();i++)
        {
            HashMap<Integer, Boolean> map = new HashMap<>();
            List<Integer> query = queries.get(i);
            int l = query.get(0);
            int r = query.get(1);
            int teams = 0;
            for(int j=l-1;j<r;j++)
            {
                if(map.containsKey(rating.get(j)) && !map.get(rating.get(j)))
                {
                    teams++;
                    map.put(rating.get(j), true);
                }
                else if(!map.containsKey(rating.get(j)))
                {
                    map.put(rating.get(j), false);
                }    
            }
            ans.add(teams);
        }
        return ans;
    }

}
public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int ratingCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> rating = IntStream.range(0, ratingCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine().replaceAll("\\s+$", "");
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .map(String::trim)
            .map(Integer::parseInt)
            .collect(toList());

        int queriesRows = Integer.parseInt(bufferedReader.readLine().trim());
        int queriesColumns = Integer.parseInt(bufferedReader.readLine().trim());

        List<List<Integer>> queries = new ArrayList<>();

        IntStream.range(0, queriesRows).forEach(i -> {
            try {
                queries.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        List<Integer> result = Result.countTeams(rating, queries);

        bufferedWriter.write(
            result.stream()
                .map(Object::toString)
                .collect(joining("\n"))
            + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}
