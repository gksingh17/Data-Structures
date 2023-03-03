import java.util.Iterator;

public class IntArray implements Iterable<Integer>{

    private static final int DEFAULT_CAP = 1 << 3;

    public int[] arr;
    public int len = 0; 
    public int capacity = 0 ; 

    //initialize the array with a default capacity 
    public IntArray(){
        this(DEFAULT_CAP); 
    }
















    public IntArray(int defaultCap) {
    }
















    @Override
    public Iterator<Integer> iterator() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'iterator'");
    }
}