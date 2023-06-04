package concepts.java;

// an annotation assigns extra metadata to the source code it's bound to. By adding an annotation to a method, 
// interface, class, or field, we can:
// Inform the compiler about warnings and errors
// Manipulate source code at compilation time
// Modify or examine behavior at runtime

// Any interface with a SAM(Single Abstract Method) is a functional interface, and its implementation may be 
// treated as lambda expressions.

@FunctionalInterface
public interface Adder {
    int add(int a, int b);
}
Adder adder = (a,b) -> a + b;
int result = adder.add(4,5);

// if we add a second method to Adder, then the compiler will complain. Even though it's legal to have more than 
// one method on an interface, it isn't when that interface is being used as a lambda target.

// There are three types of annotations.

// Marker Annotation
// Single-Value Annotation
// Multi-Value Annotation

// An annotation that has no method, is called marker annotation.
@interface MyAnnotation{}  

// An annotation that has one method, is called single-value annotation. For example:
@interface MyAnnotation{  
    int value();  
}  

// We can provide the default value also.
@interface MyAnnotation{  
    int value() default 0;  
}  
@MyAnnotation(value=10)  

// An annotation that has more than one method, is called Multi-Value annotation.
@interface MyAnnotation{  
    int value1();  
    String value2();  
    String value3();  
}  

@interface MyAnnotation{  
    int value1() default 1;  
    String value2() default "";  
    String value3() default "xyz";  
}
@MyAnnotation(value1=10,value2="Arun Kumar",value3="Ghaziabad")  
