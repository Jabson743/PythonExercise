import java.util.Scanner;
public class Task1 {
       public static void main(String... args) {
       Scanner input = new Scanner(System.in);

       int passes = 0;
       int failure = 0;
       int counter = 0;
       int userInput;

       while (true) {
       System.out.println("Enter a number between 1 or 2: ");
       userInput = input.nextInt();

       if (userInput == 1 && userInput == 2) {
           passes += 1;
           break;
        }
        else {
           failure += 1;
           System.out.println("Please enter a valid input");
       }
           System.out.println("Number of passes: " + passes);
           System.out.println("Number of failure: " + failure);
      }


 }
}