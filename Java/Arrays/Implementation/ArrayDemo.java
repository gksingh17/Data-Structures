package arrays.implementation;

import java.util.Arrays;

class ArrayDemo { 

    //search operation
    static int findElement(int arr[], int n, int key){
        for (int i = 0; i < n ; i++)
        if (arr[i]==key){
            return i; 
        }
        return -1; //not found
    }


    //function to add x in arr
    // static int[] addX(int n1, int arr[], int x){
    //     int i;
    //     int newarr[] = new int[n1 + 1];
    //     //insert the elements from old array into
    //     //new array.insert all elements till n then insert x at n+1
    //     for(i=0;i<n1;i++){
    //         newarr[i] = arr[i];
    //     }
    //     newarr[n1] = x; 
    //     return newarr; 
    // }

    // function to insert given element(key) 
    static int insertEnd(int arr[], int n, int key, int capacity){
        //cannot insert if n >= capacity
        if (n >= capacity)
            return n; 
        arr[n] = key; 

        return(n+1); 

    }

    public static void main(String[] args ) { 
        int value = 7; 

        int[] values; //refrence type 

        values = new int[3]; //3 int memory

        System.out.println(values[0]); //0 

        values[0] =10; 
        values[1] =20; 
        values[2] =30; 
        System.out.println(values[0]); //10
        System.out.println(values[1]); //20
        System.out.println(values[2]); //30 
        
        //iteration 
        for(int i = 0; i<values.length; i++){
            System.out.println(values[i]);
        }

        int[] numbers = {5,6,7}; 
        for(int i = 0; i < numbers.length; i++){
            System.out.println(numbers[i]);
        }

        //array of strings 
        String[] words =  new String[5]; 
        //set
        words[0] = "Hello";
        words[1] = "to";
        words[2] = "you";

        System.out.println(words[2]);
        String[] fruits  = {"apple", "orange", "banana", "pear"}; 

        for(String fruit: fruits){
            System.out.println(fruit);
        }

        int newvalue = 123; //primitive type
        String text = null;        // class (non primitiv), allocates memory for a refrence. 
        System.out.println(text);  // null 

        String[] texts = new String[2];
        System.out.println(texts[0]); // null 

        texts[0] = "one"; 
        System.out.println(texts[0]);


        // declares an array of integers 
        int[] anArray ; 

        //allocated memory for 10 integers
        anArray = new int[10];

        //initialize first element 
        anArray[0] = 100; 
        //initialize second element 
        anArray[1] = 200; 
        //and so on 
        anArray[2] = 300;
        anArray[3] = 400;
        anArray[4] = 500;
        anArray[5] = 600;
        anArray[6] = 700;
        anArray[7] = 800;
        anArray[8] = 900;
        anArray[9] = 1000;

        int[] newIntArray = new int[] {1,2,3,4}; 

        //shortut to create and intialize 
        String[] anArrayOfStrings = {"Gunjan", "Neo", "Neowickk"}; 
        System.out.println(anArrayOfStrings[0]);
        //length of the array is determined by the number of values provided between braces and separated by commas.
        System.out.println("Element at index 0:" + anArray[0]);
        System.out.println("Element at index 0:" + anArray[1]);

        // intialization -> dataType [] nameOfArray = new dataType [size]
        // dataType [ ] nameOfArray = {value1, value2, value3, value4}
        int[] newArray = {100, 200, 300,
        400, 500, 600, 
        700, 800, 900, 1000};

        //looping in array 
        for (int i = 0; i < newArray.length; i++ ){
            System.out.println("Element at index " + i + ":" + newArray[i]);
        }

        int arr[] = { 12, 34, 10, 6, 40 };
        int n = arr.length;
        int key = 40; 

        int positon = findElement(arr , n, key); 

          
        if (positon == -1)
            System.out.println("Element not found");
        else
            System.out.println("Element Found at Position: "
                               + (positon + 1));

        // int x = 42;
        // int n1 = arr.length + 1; 
        // arr = addX(n1, arr, x);
        // System.out.println("\nArray with " + x + " added:\n" + Arrays.toString(arr));



    }
}