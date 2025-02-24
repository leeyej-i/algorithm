package JAVA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p1205 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);
        int N = Integer.parseInt(st.nextToken());
        int newScore = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        int result = 1;
        int dupCount = 0;

        if(N == 0) {
            System.out.println(result);
            return;
        }

        input = br.readLine();
        st = new StringTokenizer(input);
        int score;
        for(int i = 0; i < N; i++){
            score = Integer.parseInt(st.nextToken());
            if (score < newScore) break;
            else if(score == newScore){
                dupCount++;
            }
            else result++;
        }

        if(result+dupCount > P) System.out.println(-1);
        else System.out.println(result);
    }
}
