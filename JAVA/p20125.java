package JAVA;

import java.awt.Point;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class p20125 {
    static int[][] board;
    static int N;
    static Point heart = new Point(0, 0);
    static int[] bodyLength = {0, 0, 0, 0, 0};
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new int[N][N];

        for(int i = 0; i < N; i++){
            String input = br.readLine();
            for(int j = 0; j < N; j++){
                char data = input.charAt(j);
                if(data == '_') board[i][j] = 0;
                else{
                    if(heart.x == 0) {
                        heart.x = i + 1;
                        heart.y = j;
                    }
                    board[i][j] = 1;
                }
            }
        }

        getBodyLength();
        System.out.println((heart.x + 1) + " " + (heart.y + 1));
        for(int i = 0; i < 5; i++){
            System.out.print(bodyLength[i] + " ");
        }
    }

    private static void getBodyLength(){

        int armLength = 0;
        for(int i = 0; i < N; i++){
            if(board[heart.x][i] == 1){
                if(i == heart.y){
                    bodyLength[0] = armLength;
                    armLength = 0;
                    continue;
                }
                armLength++;
            }
        }

        bodyLength[1] = armLength;

        for(int i = heart.x + 1; i < N; i++){
            if(board[i][heart.y] == 1)bodyLength[2]++;
            if(board[i][heart.y - 1] == 1) bodyLength[3]++;
            if(board[i][heart.y + 1] == 1) bodyLength[4]++;
        }
    }
}
