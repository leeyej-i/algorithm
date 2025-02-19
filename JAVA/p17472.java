package JAVA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Deque;
import java.util.Collections;
import java.awt.Point;
import java.util.StringTokenizer;

/* 다리 Class */
class Bridge implements Comparable<Bridge>{
    int start;
    int end;
    int cost;

    Bridge(int start, int end, int cost){
        this.start = start;
        this.end = end;
        this.cost = cost;
    }

    @Override
    public int compareTo(Bridge o){
        return this.cost - o.cost;
    } 
}

public class p17472 {
    static int[][] board;
    static int[][] visit;
    static int[] parents;
    static LinkedList<Bridge> bridges = new LinkedList<Bridge>();
    static int N;
    static int M;
    static int result = 0;

    public static void main(String args[]) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];
        visit = new int[N][M];

        for(int i = 0; i < N; i++){
            input = br.readLine();
            st = new StringTokenizer(input);
            for(int j = 0; j < M; j ++){
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        divideLand();
        makeBridge();
        findMinCost();
        
        for(int i = 1; i < parents.length; i++){
            if(getParent(parents[i]) != getParent(parents[1])){
                result = -1;
                break;
            }
        }

        System.out.println(result);

    }

    private static void divideLand(){
        int landKind = 1; 
        for(int i = 0; i< N; i++){
            for(int j = 0; j< M; j++){
                if(board[i][j] == 1 && visit[i][j] == 0){
                    visit[i][j] = 1;
                    board[i][j] = landKind;
                    bfs(i, j, landKind);
                    landKind ++;
                }
            }
        }
        parents = new int[landKind];
        for (int i = 1; i < landKind; i++){
            parents[i] = i;
        }
    }

    private static void bfs(int x, int y, int landNumber){
        int dx[] = {0, 1, 0, -1};
        int dy[] = {1, 0, -1, 0};

        Deque<Point> deque = new LinkedList<Point>();
        deque.add(new Point(x,y));
        int newX, newY;

        while(!deque.isEmpty()){
            Point point = deque.pollFirst();
            x = point.x;
            y = point.y;

            for(int i = 0; i < 4; i++){
                newX = x + dx[i];
                newY = y + dy[i];
                if(0 <= newX && newX < N && 0 <= newY && newY < M){
                    if(visit[newX][newY] == 0 && board[newX][newY] == 1){
                        visit[newX][newY] = 1;
                        board[newX][newY] = landNumber;
                        deque.add(new Point(newX, newY));

                    }
                }
            }
        }
    }

    private static void makeBridge(){
        for(int i = 0; i < N; i ++){
            for(int j = 0; j< M; j++){
                if(board[i][j] > 0){
                    int cost = 0;
                    for(int k = j + 1; k < M; k++){
                        if(board[i][j] == board[i][k]) break;
                        else if(board[i][k] == 0) cost++;
                        else{
                            if(cost >= 2){
                                bridges.add(new Bridge(board[i][j], board[i][k], cost));
                            }
                            break;
                        }
                    }

                    cost = 0;
                    for(int k = i + 1; k < N; k++){
                        if(board[i][j] == board[k][j]) break;
                        else if(board[k][j] == 0) cost++;
                        else{
                            if(cost >= 2){
                                bridges.add(new Bridge(board[i][j], board[k][j], cost));
                            }
                            break;
                        }
                    }
                }
            }
        }
    }

    private static void findMinCost(){
        int totalCost = 0;
        Collections.sort(bridges);
        while(!bridges.isEmpty()){
            Bridge bridge = bridges.pollFirst();
            if(getParent(bridge.start) != getParent(bridge.end)){
                totalCost += bridge.cost;
                union(bridge.start, bridge.end);
            }
        }
        result = totalCost;
    }

    private static int getParent(int bridgeKind){
        if(parents[bridgeKind] == bridgeKind) return bridgeKind;

        return getParent(parents[bridgeKind]);
    }

    private static void union(int start, int end){
        start = getParent(start);
        end = getParent(end);

        if(start != end){
            parents[end] = getParent(start);
        }
    }



}   
