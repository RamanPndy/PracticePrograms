import java.util.HashMap;
import java.util.Map;

public class Main {
    public static String KUniqueCharacters(String str) {
        int k = Character.getNumericValue(str.charAt(0));
        str = str.substring(1); // Remove the first character (k) from the string
        int n = str.length();
        if (n < k) {
            return "";
        }

        int left = 0;
        int right = 0;
        int max_length = 0;
        String max_substring = "";

        // Map to keep track of character frequencies within the window
        Map<Character, Integer> charFreq = new HashMap<>();

        while (right < n) {
            // Expand the window to the right
            char c = str.charAt(right);
            charFreq.put(c, charFreq.getOrDefault(c, 0) + 1);

            // Shrink the window from the left if the number of unique characters exceeds k
            while (charFreq.size() > k) {
                char leftChar = str.charAt(left);
                charFreq.put(leftChar, charFreq.get(leftChar) - 1);
                if (charFreq.get(leftChar) == 0) {
                    charFreq.remove(leftChar);
                }
                left++;
            }

            // Check if the current window is the longest encountered so far
            int current_length = right - left + 1;
            if (current_length > max_length) {
                max_length = current_length;
                max_substring = str.substring(left, right + 1);
            }

            right++;
        }

        return max_substring;
    }

    public static void main(String[] args) {
        System.out.println(KUniqueCharacters("2aabbacbaa")); // Output: "aabba"
    }
}
