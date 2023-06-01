import java.util.ArrayList;
import java.util.List;

public class DirectoryTraversal {
    public static List<String> getFilesStartingWithA(Node node) {
        List<String> result = new ArrayList<>();
        dfs(node, result);
        return result;
    }

    private static void dfs(Node node, List<String> result) {
        if (node == null) {
            return;
        }

        if (node.type.equalsIgnoreCase("file") && node.name.toLowerCase().startsWith("a")) {
            result.add(node.name);
        }

        if (node.children != null) {
            for (Node child : node.children) {
                dfs(child, result);
            }
        }
    }

    public static void main(String[] args) {
        // Example usage
        Node rootNode = new Node();
        rootNode.type = "dir";
        rootNode.name = "root";
        rootNode.children = new Node[3];

        Node file1 = new Node();
        file1.type = "file";
        file1.name = "apple.txt";

        Node file2 = new Node();
        file2.type = "file";
        file2.name = "banana.txt";

        Node file3 = new Node();
        file3.type = "file";
        file3.name = "orange.txt";

        rootNode.children[0] = file1;
        rootNode.children[1] = file2;
        rootNode.children[2] = file3;

        List<String> filesStartingWithA = getFilesStartingWithA(rootNode);
        System.out.println(filesStartingWithA);  // Output: [apple.txt]
    }
}
