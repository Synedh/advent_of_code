const coords = require('fs')
    .readFileSync('input', { encoding: 'utf-8' })
    .split('\n')
    .reduce(({ x, y, aim }, value) => {
        let [way, qty] = value.split(' ')
        qty = parseInt(qty);
        if (way === 'forward') {
            return { x: x + qty, y: y + x * aim, aim };
        }
        if (way === 'up') {
            return { x, y, aim: aim - qty };
        }
        if (way === 'down') {
            return { x, y, aim: aim + qty };
        }
        return { x, y }
    }, { x: 0, y: 0, aim: 0 });
console.log(coords.x * coords.y);
