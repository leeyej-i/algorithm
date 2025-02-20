package JAVA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p5073 {
    public static void main(String args[]) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while(true){
            String input = br.readLine();
            StringTokenizer st = new StringTokenizer(input);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if(a == 0 && a == b && b == c){
                break;
            }

            if(!isTriangle(a, b, c)){
                System.out.println("Invalid");
                continue;
            }

            if(a == b && b == c) {
                System.out.println("Equilateral");
                continue;
            }

            if(a == b || b == c || a == c){
                System.out.println("Isosceles");
                continue;
            }

            System.out.println("Scalene");
        }
    }

    private static boolean isTriangle(int a, int b, int c){
        int count = 0;
        if(a < (b + c)) count++;
        if(b < (c + a)) count++;
        if(c < (a + b)) count++;

        if(count == 3) return true; 
        else return false;
    }
}
