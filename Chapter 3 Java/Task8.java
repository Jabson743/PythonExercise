import java.util.Scanner;
public class Task8 {
       public static void main(String... args) {
       Scanner input = new Scanner(System.in);

       System.out.print("Enter your first integer: ");
       int number1 = input.nextInt();

       System.out.print("Enter your second integer: ");
       int number2 = input.nextInt();

       System.out.print("Enter your third integer: ");
       int number3 = input.nextInt();

       int sum = number1 + number2 + number3;
       int average = sum / 3;
       int product = number1 * number2 * number3;

       System.out.println("The sum of the integer is: " + sum);
       System.out.println("The average of the integer is: " + average);
       System.out.println("The product of the integer is: " + product);

}

}