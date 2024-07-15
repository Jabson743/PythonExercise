import java.util.Scanner;
public class Task11 {
       public static void main(String... args) {
       Scanner input = new Scanner(System.in);

       System.out.print("Enter the gallon used(-1 to to end): ");
       float gallonUsed = input.nextFloat();

       System.out.print("Enter the miles driven: ");
       int milesDriven = input.nextInt();

       if (gallonUsed != -1) {
       
       float milesPerGallon = milesDriven / gallonUsed;

       System.out.print(milesPerGallon);
       
       
       }

 }
}