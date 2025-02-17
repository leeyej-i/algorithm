package JAVA;
/**
 * 백준 16637 문제
 * 골드 4 / 뱀
 **/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
public class p16637{
    static int result = Integer.MIN_VALUE;;
    static ArrayList<Integer> nums = new ArrayList<>();
    static ArrayList<Character> opts = new ArrayList<>();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String calString = br.readLine();
        for(int i = 0; i < N; i++){
            char calChar = calString.charAt(i);
            if(calChar == '+' || calChar == '-' || calChar == '*') opts.add(calChar);
            else nums.add((int)(calChar-'0'));
        } 
        // INDEX, 괄호 사용여부, INDEX - 2연산결과, INDEX - 1의 연산결과
        dfs(0, 0, nums.get(0), nums.get(0));
        System.out.println(result);
    }
    private static void dfs(int optIdx, int isUsed, int result1, int result2){
        //연산자 INDEX가 초과하면 종료
        if(optIdx >= opts.size()) {
            result = Math.max(result2, result);
            return;
        }                                                                                                                                                                                                                                                                                                                                                                                                                     
        //바로 앞의 부호에서 괄호를 사용했는지 체크
        //사용안했으면 뒤의 연산은 괄호를 사용해도 되고 안해도 된다.
        int newResult;
        if(isUsed == 0){
            // 괄호를 사용하지 않은 것
            newResult = calc(result2, opts.get(optIdx), nums.get(optIdx + 1));
            dfs(optIdx + 1, 0, result2, newResult);
            // 괄호를 사용한 것(제일 처음은 안됨)
            if(optIdx > 0){
                newResult = calc(result1, opts.get(optIdx-1), calc(nums.get(optIdx), opts.get(optIdx), nums.get(optIdx + 1)));
                dfs(optIdx + 1, 1, result1, newResult);
            }
        }
        //사용했으면 뒤의 연산은 괄호를 무조건 사용할 수 없다.
        else if(isUsed == 1){
            newResult = calc(result2, opts.get(optIdx), nums.get(optIdx + 1)  );
            dfs(optIdx + 1, 0, result2, newResult);
        }

    }

    private static int calc(int firstNum, char opt, int secondNum){
        if(opt == '+') return firstNum + secondNum;
        else if(opt == '-') return firstNum - secondNum;
        else if(opt == '*') return firstNum * secondNum;
        else return 0;
    }
 }