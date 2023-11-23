// https://school.programmers.co.kr/learn/courses/30/lessons/250137?language=javascript
function solution(bandage, health, attacks) {
  const [t, x, y] = bandage;

  const attackTime = [];
  const damage = [];

  attacks.forEach((v) => {
    const [a, b] = v;
    attackTime.push(a);
    damage.push(b);
  });

  let playerHealth = health;
  let bonus = 0;

  const arr = Array.from(
    { length: attackTime[attackTime.length - 1] },
    (_, i) => i + 1
  );

  for (v of arr) {
    if (attackTime.includes(v)) {
      bonus = 0;
      playerHealth -= damage[attackTime.indexOf(v)];
      if (playerHealth <= 0) return -1;
      continue;
    }
    if (playerHealth < health) {
      bonus += 1;
      playerHealth += x;
    }
    if (bonus == t) {
      bonus = 0;
      playerHealth += y;
    }
    if (playerHealth > health) {
      playerHealth = health;
    }
  }
  return playerHealth;
}

console.log(
  solution([5, 1, 5], 30, [
    [2, 10],
    [9, 15],
    [10, 5],
    [11, 5],
  ])
);
