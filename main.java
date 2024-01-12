import java.util.*;
import java.io.*;

public class main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s;
        int count = 0, n = 0, rand;
        char arr[] = new char[5];
        char arr2[] = new char[5];
        boolean guess = true;
        for (int i = 0; i < 5; i ++) {
            rand = (int) Math.floor(Math.random() *(122 - 97 + 1) + 97);
            arr2[i] = (char) rand;
        }
        while (guess) {
            System.out.println("Input Guess");
            count = 0;
            s = scan.nextLine();
            if (s.length() == 5) {
                n ++;
                for (int j = 0; j < 5; j ++) {
                    System.out.print(s.charAt(j)+" ");
                    arr[j] = s.charAt(j);
                }
                System.out.println();
                for (int j = 0; j < 5; j ++) {
                    if (arr[j] == arr2[j]) {
                        System.out.print("✓ ");
                        count ++;
                    }
                    else {
                        System.out.print("X ");
                    }
                }
                System.out.println();
                if (count == 5) {
                    guess = false;
                }
            }
            else {
                System.out.println("Invalid guess");
            }
        }
        System.out.println("You guyessed the code in "+ n +" steps!");
    }
}