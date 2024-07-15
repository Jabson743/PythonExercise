import java.util.Scanner;
public class CornFlakes {
       public static void main(String... args) {
       Scanner input = new Scanner(System.in);

       System.out.print("Enter a number: ");
       int number = input.nextInt();

       for(int counter = 1; counter <= 10; counter++) {
  
       int result = number * counter;

        System.out.println(number + " * " + counter + " = " + result);
     
       }
  }
}