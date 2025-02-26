package JAVA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p21921 {
    static int N, X;
    static int[] visitor;
    static int result;
    static int count = 1;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());

        visitor = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++){
            visitor[i] = Integer.parseInt(st.nextToken());
            if(i < X){
                result += visitor[i];
            }
        }
        getMaxVisitors();
        if(result == 0) {
            System.out.println("SAD");
            return;
        }
        System.out.println(result);
        System.out.println(count);

    }   

    private static void getMaxVisitors(){
        int sum = result;
        for(int i = 1; i < N; i++){
            if(i + X - 1 < N){
                sum = sum - visitor[i - 1] + visitor[i + X - 1];
                if(sum == result){
                    count++;
                }
                else if(sum > result){
                    result = sum;
                    count = 1;
                }
            }
            else break;
        }
    }
}
