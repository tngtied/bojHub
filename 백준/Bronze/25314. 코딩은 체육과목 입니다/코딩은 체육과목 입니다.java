import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		while (n > 4) {
			System.out.print("long ");
			n -= 4;
		}
		System.out.print("long int");

	}

}