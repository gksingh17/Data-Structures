class ArrayDemo { 
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


    }
}