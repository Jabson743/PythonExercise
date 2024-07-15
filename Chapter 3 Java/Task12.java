import java.util.Scanner;
public class Task12 {
       public static void main(String... args) {
       Scanner input = new Scanner(System.in);

       System.out.print("Enter a five-digit integer: ");
       int number = input.nextInt();

       int firstNumber = (number / 10000);
       int secondNumber = (number / 1000) % 10;
       int thirdNumber = (number / 100) % 10;
       int fourthNumber = (number / 10) % 10;
       int fifthNumber = number % 10;

       if (firstNumber == fifthNumber && secondNumber == fourthNumber) {
       System.out.println(number + " is a palindrome");
       }
       else {
       System.out.println(number + " is not a palindrome");
       }

  }
  
}