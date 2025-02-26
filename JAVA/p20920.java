package JAVA;

import java.util.List;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class p20920 {
    public static void main(String args[]) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Map<String, Integer> dict = new HashMap<>();
        for(int i = 0; i < N; i++){
            String words = br.readLine();
            if(words.length() < M) continue;
            dict.put(words, dict.getOrDefault(words, 1)+ 1);
        }

        List<Map.Entry<String, Integer>> sortList = new ArrayList<>(dict.entrySet());
        sortList.sort((a, b) -> {
            if(a.getValue() != b.getValue()) return b.getValue() - a.getValue();
            else if(a.getKey().length() != b.getKey().length()) return b.getKey().length() - a.getKey().length();
            return a.getKey().compareTo(b.getKey());
        });

        for(int i = 0; i < sortList.size(); i++){
            bw.write(sortList.get(i).getKey() + "\n");
        }
        bw.flush();
        bw.close();
    }
}
 