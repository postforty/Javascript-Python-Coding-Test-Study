function solution(people, limit) {
  var answer = 0;

  people = people.sort((a, b) => a - b);
  let left = 0;
  let right = people.length - 1;

  while (left <= right) {
    if (people[left] + people[right] <= limit) {
      left++;
      right--;
    } else {
      right--;
    }
    answer++;
  }

  return answer;
}

console.log(solution([70, 50, 80, 50], 100));
