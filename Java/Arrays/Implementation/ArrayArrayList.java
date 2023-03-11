package arrays.implementation;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ArrayArrayList {
    public static void main(String[] args) {
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        //adding  
        numbers.add(10);
        numbers.add(50);
        numbers.add(51);
        

        // reteriving 
        System.out.println(numbers.get(1));

        // Indexed for loop iteration
        System.out.println("\nIteration #1: "); 
        for(int i = 0;i <numbers.size(); i++){
            System.out.println(numbers.get(i));
        }

        
        //removing 
        //last element remove 
        // be careful while removing 
        numbers.remove(numbers.size() - 1); 

        //this is very slow 
        numbers.remove(0); 

        //iteration number 2 
        System.out.println("\nIteration #2: ");
        for(Integer value: numbers ){
            System.out.println(value);
        }

        String[] peoplenames = { "neo","trinity", "smith", "morpheous", "oracle" }; 

        //LIST Interface 
        List<String> values = new ArrayList<String>(); 

        ArrayList<String> names = new ArrayList<String>();
        for (int i = 0 ; i<5 ; i++) {
            names.add(peoplenames[i]);
        }
        System.out.println(names);
    }

    
}
