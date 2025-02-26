package JAVA;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class p9017 {
    static int N;
    static int minSum;
    static int fifthScore;
    static int result;
    static int[] scoreCount ;
    static int[] scoreList;
    public static void main(String[] args)throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int i = 0; i < T; i++){
            minSum = 4000;
            fifthScore = 1000;
            N = Integer.parseInt(br.readLine());
            String input = br.readLine();
            StringTokenizer st = new StringTokenizer(input);

            ArrayList<Integer> sixMemberTeamList = new ArrayList<Integer>();
            scoreCount = new int[200 + 1];
            scoreList = new int[N + 1];
            for(int j = 0; j < N; j++){
                int team = Integer.parseInt(st.nextToken());
                scoreCount[team] ++;
                scoreList[j] = team;
            }

            for(int j = 1; j < 201; j++){
                if(scoreCount[j] == 0) break;
                else if(scoreCount[j] == 6) sixMemberTeamList.add(j);
            }
            int rank = 1;
            int[][] sixMemberTeamScore = new int[201][2];
            for(int j = 0; j < N; j++){
                int teamNum = scoreList[j];
                sixMemberTeamScore[teamNum][1] ++;
                if(sixMemberTeamList.contains(teamNum)) {
                    if(sixMemberTeamScore[teamNum][1] <= 4) sixMemberTeamScore[teamNum][0] += rank;
                    else if(sixMemberTeamScore[teamNum][1] == 5){
                        if(sixMemberTeamScore[teamNum][0] < minSum){
                            minSum = sixMemberTeamScore[teamNum][0];
                            result = teamNum;
                            fifthScore = rank;
                        }
                        else if(sixMemberTeamScore[teamNum][0] == minSum){
                            if(rank < fifthScore){
                                fifthScore = rank;
                                result = teamNum;
                            }
                        }
                    }
                    rank ++; 
                }
                
            }
            System.out.println(result);
        }
    }
}

