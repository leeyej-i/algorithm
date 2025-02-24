package JAVA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class p25757 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);
        int N = Integer.parseInt(st.nextToken());
        char game = st.nextToken().charAt(0);

        int gameUser = 0;
        if(game == 'Y') gameUser = 1;
        if(game == 'F') gameUser = 2;
        if(game == 'O') gameUser = 3;

        Set<String> userSet = new HashSet<>();
        for(int i = 0; i < N; i++){
            String user = br.readLine();
            userSet.add(user);
        }

        System.out.println(userSet.size() / gameUser);
    }
}
