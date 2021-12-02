console.log(
    require('fs')
        .readFileSync('input', { encoding: 'utf-8' })
        .split('\n')
        .map((value) => { return { way: value.split(' ')[0], qty: value.split(' ')[1] }; })
        .reduce(({ x, y }, value) => {
            if (value.way === 'forward') {
                return { x: x + value.qty, y };
            }
            if (value.way === 'up') {
                return { x, y: y - value.qty };
            }
            if (value.way === 'down') {
                return { x, y: y + value.qty };
            }
            return { x, y }
        }, { x: 0, y: 0 })
);