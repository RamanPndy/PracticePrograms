// A marker interface is an interface that doesn't have any methods or constants inside it. 
// It provides run-time type information about objects, so the compiler and JVM have additional information 
// about the object.
// A marker interface is also called a tagging interface.
// Though marker interfaces are still in use, they very likely point to a code smell, and we should use them 
// carefully. The main reason for this is that they blur the lines of what an interface represents, since 
// markers don't define any behavior. 
// Newer development favors annotations to solve some of the same problems.
// Java has many built-in marker interfaces, such as Serializable, Cloneable, and Remote.

// If we try to clone an object that doesn't implement Cloneable interface, the JVM throws a 
// CloneNotSupportedException. Thus, the Cloneable marker interface is an indicator to the JVM that we can call 
// the Object.clone() method.

// Unlike annotations, interfaces allow us to take advantage of polymorphism. As a result, we can add additional 
// restrictions to the marker interface.

// we can achieve the same results by using a typical interface as a marker, we'll end up with a poor design.

public interface Deletable {
}

public class Entity implements Deletable {
    // implementation details
}

public class ShapeDao {

    // other dao methods

    public boolean delete(Object object) {
        // we're giving an indication to the JVM about the runtime behavior of our objects. 
        if (!(object instanceof Deletable)) {
            return false;
        }

        // delete implementation details
        
        return true;
    }
}
