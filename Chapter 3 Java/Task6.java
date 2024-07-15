import java.util.Scanner;
public class Task6 {
       public static void main(String... args) {
       Scanner input = new Scanner(System.in);

       System.out.println("What is your problem?.");
       String answer = input.nextLine();

       System.out.println("Have you had this kind of problem before(yes/no)?");
       String reply = input.nextLine();

       if (reply == "yes") {
       System.out.print("Well, you have it again.");
       } 

       else {
       System.out.print("Well, you have it now.");
       }
 }
}