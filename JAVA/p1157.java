package JAVA;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class p1157 { 
    public static void main(String args[]) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine().toUpperCase();
        int[] alpabets = new int[26];

        for(int i = 0; i < input.length(); i++){
            char text = input.charAt(i);
            alpabets[(int)text - 65]++;
        }

        int maxCount = 0;
        boolean dupCheck = false;
        char result = '?';
        for(int i = 0; i < 26; i++){
            if(alpabets[i] > maxCount){
                maxCount = alpabets[i];
                dupCheck = false;
                result = (char)(i + 65);
            }
            else if(alpabets[i] == maxCount){
                dupCheck = true;
            }
        }

        if(dupCheck == false) System.out.println(result);
        else System.out.println("?");

    }    
}
