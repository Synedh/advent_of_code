const cards = require('fs').readFileSync('input', "utf8").split('\n').filter(e => e.length);

let total = 0;
const occurences = Array(cards.length).fill(1);
for (const [i, card] of cards.entries()) {
    const [winnings, pulled] = card.split(':')[1].split('|').map(e => e.split(' ').filter(e => e));
    const valids = winnings.filter(e => pulled.includes(e)).length;

    total += parseInt(2 ** (valids - 1));
    for (const j of Array(valids).keys()) {
        occurences[i + j + 1] += occurences[i];
    }
}
console.log(total, occurences.reduce((total, val) => total + val, 0));
