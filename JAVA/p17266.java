package JAVA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p17266 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        double first = 0;
        double second = 0;
        int maxDistance = 0;

        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);

        for(int i = 0; i < M; i++){
            second = Integer.parseInt(st.nextToken());
            if(i == 0) maxDistance = Math.max(maxDistance, (int)(second - first));
            else maxDistance = Math.max(maxDistance, (int)Math.ceil((second - first) / 2));
            first = second;
        }

        second = N;
        maxDistance = Math.max(maxDistance, (int)(second - first));

        System.out.println(maxDistance);
    }
}
