package baekjun;

import java.util.Scanner;

public class BOJ2439 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		for(int i=1; i <= a; i++) {
			System.out.println(" ".repeat(a-i) + "*".repeat(i));		
		}
	}
}
