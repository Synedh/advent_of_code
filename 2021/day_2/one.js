const coords = require('fs')
    .readFileSync('input', { encoding: 'utf-8' })
    .split('\n')
    .reduce(({ x, y }, value) => {
        let [way, qty] = value.split(' ')
        qty = parseInt(qty);
        if (way === 'forward') {
            return { x: x + qty, y };
        }
        if (way === 'up') {
            return { x, y: y - qty };
        }
        if (way === 'down') {
            return { x, y: y + qty };
        }
        return { x, y }
    }, { x: 0, y: 0 });
console.log(coords.x * coords.y);
