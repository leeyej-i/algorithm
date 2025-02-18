package JAVA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p17136 {
    static int paper[] = {0, 0, 0, 0, 0}; 
    static char[][] board = new char[10][10];
    static int result = 26;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for(int i = 0; i < 10; i++){
            String input = br.readLine();
            StringTokenizer st = new StringTokenizer(input);
            for(int j = 0; j < 10; j++){
                char num = st.nextToken().charAt(0);
                board[i][j] = num;
            }
        }
        //x, y, paperCount
        dfs(0, 0, 0);
        if (result == 26) result = -1;
        System.out.println(result);
    }

    private static void dfs(int row, int col, int paperCount){
        /* 조건 
         * 1) 행이 범위를 벗어날 때 종료
         * 2) 종이 25개 내에서 다 탐색했을 때 최소값 업데이트
         * 3) 열이 범위를 벗어날 때 행 증가
         * 4) 종이 최소값을 벗어나면 종료
         * 5) 종이를 붙일 수 있으면 count 증가 후 DFS
         * 6) 종이를 붙일 수 없으면 다음 탐색
         */
        if(row == 10) return;
        if(row == 9 && col == 10){
            result = Math.min(result, paperCount);
            return;
        }
        if(col == 10){
            dfs(row+1, 0, paperCount);
            return;
        };
        if(paperCount >= result) return;

        if(board[row][col] == '1'){
            for(int i = 0; i < 5; i++){
                if(paper[i] < 5){
                    if(attachPaper(row, col, i) == 1){
                        dfs(row, col+1, paperCount + 1);
                        tearPaper(row, col, i);
                    }
                }

            }
        }
        else {
            dfs(row, col + 1, paperCount);
        }
    
    }

    private static int attachPaper(int row, int col, int paperSize){
        if((row + paperSize + 1) > 10 || (col + paperSize + 1) > 10) return 0;
        for(int i = row; i < row + paperSize + 1; i++){
            for(int j = col; j < col + paperSize + 1; j++){
                if(board[i][j] == '0') return 0;
            }
        }
        for(int i = row; i < row + paperSize + 1; i++){
            for(int j = col; j < col + paperSize + 1; j++){
                if(board[i][j] == '1') board[i][j] = '0';
            }
        }

        paper[paperSize]++;
        return 1;
    }

    private static void tearPaper(int row, int col, int paperSize){
        for(int i = row; i < row + paperSize + 1; i++){
            for(int j = col; j < col + paperSize + 1; j++){
                board[i][j] = '1';
            }
        }

        paper[paperSize]--;
    }



    
}
