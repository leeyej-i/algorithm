package JAVA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p10431 {
    static int T;
    static int[] resultArray;
    static int[] students;
    public static void main(String args[]) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        resultArray = new int[T+1];

        for(int i = 0; i < T; i++){
            String input = br.readLine();
            StringTokenizer st = new StringTokenizer(input);
            int index = Integer.parseInt(st.nextToken());
            students = new int[20];
            for(int j = 0; j < 20; j++){
                students[j] = Integer.parseInt(st.nextToken());
            }

            lineUp(index);
        }

        for(int i = 1; i < T+1; i++){
            System.out.println(i + " " + resultArray[i]);
        }
    }
    
    private static void lineUp(int index){

        int changeStundent = 0;
        int subResult = 0;
        for(int i = 1; i < 20; i++){
            if(students[i] < students[i-1]){
                changeStundent = students[i];
                subResult = 0;
                for(int j = i - 1; j >= 0; j--){
                    if(students[j] > changeStundent){
                        students[j+1] = students[j];
                        subResult++;
                    }
                }

                students[i - subResult] = changeStundent;
                resultArray[index]+= subResult;

            }
        }
    }
}
