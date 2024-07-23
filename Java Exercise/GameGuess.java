import java.util.Scanner;
import java.util.Random;
public class GameGuess {
       public static void main(String... args) {
       Scanner input = new Scanner(System.in);

       Random rand = new Random();

       System.out.print("Enter a random number: ");
       int number = rand.nextInt(1, 10);

       System.out.print(number);

  }
}