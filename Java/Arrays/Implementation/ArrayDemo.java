package Arrays.Implementation;
class ArrayDemo { 

    //search operation
    static int findElement(int arr[], int n, int key){
        for (int i = 0; i < n ; i++)
        if (arr[i]==key){
            return i; 
        }
        return -1; //not found
    }

    // function to insert given element(key) 
    static int insertEnd(int arr[], int n, int key, int capacity){
        //cannot insert if n >= capacity
        if (n >= capacity)
            return n; 
        arr[n] = key; 

        return(n+1); 

    }



    public static void main(String[] args ) { 
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

        

    }
}