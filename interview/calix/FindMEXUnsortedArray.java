// To find the Minimum Excluded Element (MEX) in an unsorted array of integers in O(n) time complexity, you can modify the counting technique typically used for finding MEX.

// Here's the modified algorithm:

// Iterate through the given array, and for each element num in the array:

// If num is non-negative and less than the array size n, swap num with the element at index num. This step ensures that each non-negative integer num in the array is moved to its corresponding index num if possible.
// Iterate from 0 to n (exclusive), and find the first index i where arr[i] is not equal to i. This index represents the MEX of the array.

// If all elements from 0 to n (exclusive) are equal to their corresponding indices, the MEX is equal to n.
public class Main {
    public static int findMEX(int[] arr) {
        int n = arr.length;

        // Rearrange elements in the array
        for (int i = 0; i < n; i++) {
            while (arr[i] >= 0 && arr[i] < n && arr[i] != i && arr[i] != arr[arr[i]]) {
                // Swap arr[i] with arr[arr[i]]
                int temp = arr[i];
                arr[i] = arr[temp];
                arr[temp] = temp;
            }
        }

        // Find the first index i where arr[i] is not equal to i
        for (int i = 0; i < n; i++) {
            if (arr[i] != i) {
                return i;
            }
        }

        // If all elements from 0 to n-1 are equal to their corresponding indices, return n
        return n;
    }

    public static void main(String[] args) {
        int[] arr = {3, 0, 1, 4, 2};
        System.out.println(findMEX(arr));  // Output: 5
    }
}
