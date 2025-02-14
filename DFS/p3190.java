/**
 * 백준 3190번 문제
 * 골드 4 / 뱀
 **/

 import java.io.BufferedReader;
 import java.io.InputStreamReader;
 import java.util.LinkedList;
 import java.util.Deque;
 import java.awt.Point;
 import java.util.StringTokenizer;
 public class p3190{
     private static int N;
     public static void main(String[] args) throws Exception {
         int result = 0;
         int subResult = 0;
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         N = Integer.parseInt(br.readLine());
         int K = Integer.parseInt(br.readLine());
         int[][] board = new int[N][N];
         Deque<Point> deque = new LinkedList<Point>();
         deque.add(new Point(0,0));
         /*
          * 뱀     : 1
          * 사과   : 2
          */
 
         for (int i = 0; i < K; i++){
             StringTokenizer st = new StringTokenizer(br.readLine());
             int row = Integer.parseInt(st.nextToken());
             int col = Integer.parseInt(st.nextToken());
             board[row-1][col-1] = 2;
         }
 
         int L = Integer.parseInt(br.readLine());
         int snakeVector = 0;
         for (int i = 0; i < L; i++){
             StringTokenizer st = new StringTokenizer(br.readLine());
             int time = Integer.parseInt(st.nextToken());
             char vector = st.nextToken().charAt(0);
             time = time - result;
             subResult = playDummy(board, deque, time, snakeVector);
             result += subResult;
             if(subResult < time)  {
                 System.out.print(result+1);
                 return;
             };
             if (vector == 'D')
                 snakeVector ++;
             else 
                 snakeVector --;
             
             if (snakeVector == -1) snakeVector = 3;
             else if(snakeVector == 4) snakeVector = 0;
         }
         subResult = playDummy(board, deque, N+1, snakeVector);
         result += subResult;
         System.out.println(result+1);
     }
 
     private static int playDummy(int[][] board, Deque<Point> deque, int time, int vector){
         int dx[] = {0, 1, 0, -1};
         int dy[] = {1, 0, -1, 0};
         int seconds = 0;
         while(seconds < time){
             seconds++;
             Point snakeHead = deque.getLast();
             int snakeX = snakeHead.x;
             int snakeY = snakeHead.y;
             int newSnakeX = snakeX + dx[vector];
             int newSnakeY = snakeY + dy[vector];
             if(newSnakeX == -1 || newSnakeY == -1 || newSnakeX == N || newSnakeY == N){
                 seconds--;
                 break;
             }
             else if (board[newSnakeX][newSnakeY] == 2){
                 board[newSnakeX][newSnakeY] = 1;
                 deque.addLast(new Point(newSnakeX, newSnakeY));
             }
             else if(board[newSnakeX][newSnakeY] == 1){
                 seconds--;
                 break;
             }
             else {
                 board[newSnakeX][newSnakeY] = 1;
                 deque.addLast(new Point(newSnakeX, newSnakeY));
                 Point snakeTail = deque.pollFirst();
                 board[snakeTail.x][snakeTail.y] = 0;
             }
         }
         return seconds;
     }
  }