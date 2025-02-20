package JAVA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p23971 {
    static int H, W, N, M;
    public static void main(String args[]) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);
        H = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int result = getMaxPeople();
        System.out.println(result);
    }

    private static int getMaxPeople(){
        int maxCount = 0;
        int rowCount, colCount;

        rowCount = 1 + ((H - 1) / (N + 1));
        colCount = 1 + ((W - 1) / (M + 1));

        maxCount = rowCount * colCount;
        return maxCount;
    }
    
}
