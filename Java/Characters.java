public class Characters {
    
    public int id ; 
    public String name; 
    public int universe; 

    Characters(int id, String name, int universe){
        this.id = id ;
        this.name = name; 
        this.universe = universe; 
    }

    public static void main(String[] args) {

        Characters[] charArrayOne = new Characters[]{new Characters(1, "ironman", 612 ),
        new Characters(2, "spiderman", 712)};


        Characters[] charArrayTwo = new Characters[5]; // initializing and allocating memory 
        charArrayTwo[0] = new Characters(0, "neo", 0); 
        charArrayTwo[1] = new Characters(1, "agent smith", 0); 

        for(Characters c:charArrayOne){    
            System.out.println(c.name);
        }


    }

}
