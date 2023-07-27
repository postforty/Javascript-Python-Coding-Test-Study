class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        return answer;
    }
}

public class Test {
    public static void main(String[] args) {
        Solution s = new Solution();
        String[] participants = {"mislav", "stanko", "mislav", "ana"};
        String[] completions = {"stanko", "ana", "mislav"};
        String result = s.solution(participants, completions);
        System.out.println(result);
    }
}