package baekjun;

import java.util.Scanner;

public class BOJ10818 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int size = sc.nextInt();
		int[] nums = new int[size];
		for(int i = 0; i<size; i++) {
			nums[i] = sc.nextInt();
		}
		int max = nums[0];
		int min = nums[0];
		for(int i = 1; i < nums.length; i++){
			if (nums[i]<min) {
				min = nums[i];
			}
			if (nums[i]>max) {
				max = nums[i];
			}
		}
		System.out.printf("%d %d", min, max);
	}
}
