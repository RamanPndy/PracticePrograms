// To find the Minimum Excluded Element (MEX) in an array of integers in O(n) time complexity, you can use the following algorithm:

// Create a boolean array visited of size n+1 and initialize all its elements to false. The visited array will be used to mark the presence of elements in the given array.
// Iterate through the given array, and for each element num in the array:
// If num is in the range [0, n] (inclusive), mark visited[num] as true.
// Iterate from 0 to n (exclusive), and find the first index i where visited[i] is false. This index represents the MEX of the array.
// Return the MEX.
public class Main {
    public static int findMEX(int[] arr) {
        int n = arr.length;
        boolean[] visited = new boolean[n + 1];

        // Mark elements in the given array as visited
        for (int num : arr) {
            if (num >= 0 && num <= n) {
                visited[num] = true;
            }
        }

        // Find the first index i where visited[i] is false
        for (int i = 0; i <= n; i++) {
            if (!visited[i]) {
                return i;
            }
        }

        // If all elements from 0 to n (inclusive) are visited, return n+1
        return n + 1;
    }

    public static void main(String[] args) {
        int[] arr = {0, 1, 3, 5, 6};
        System.out.println(findMEX(arr));  // Output: 2
    }
}
