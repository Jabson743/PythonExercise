import java.util.Scanner;
public class BankAccount {
       public static void main(String... args) {
       Scanner input = new Scanner(System.in);

       System.out.println("Welcome to your online banking");
       System.out.print("Enter your name: ");
       String name = input.nextLine();

	int deposit = 0;
	int withdraw = 0;
	int balance = 0;	
	int newBalance = 0;
           
       while (true) {
       String account = """
                      1. Deposit
                      2. Withdraw
                      3. Balance
                      99. Quit
                      """; 
      System.out.println(account);

      System.out.println("Enter 1 or 99 to quit: ");
      int number = input.nextInt();   
      
      switch (number) {

      case 1:
      System.out.println("Deposit");
      System.out.print("Enter the amount you wish to deposit: ");
      number = input.nextInt();
      balance += number;
      System.out.printf("Your account Balance is %d%n", balance);
      break;

      case 2:
      System.out.println("Withdraw");
      System.out.print("Enter the amount you wish to withdraw: ");
      number = input.nextInt();
	
      if (withdraw <= 0) {
         System.out.println("Invalid amount!!!,amount should be greater than zero");
	}

	else if (withdraw > balance) {
		System.out.println(" Insufficient funds");
	}

	else{
		newBalance = balance - number;
	}
      break;
      
      case 3:
      System.out.println("Balance");
	newBalance += balance;
      System.out.printf("Your account Balance is %d%n", newBalance);
      break;

      case 99:
      System.out.println("Thanks for banking with us");


      }

    }

  }
}