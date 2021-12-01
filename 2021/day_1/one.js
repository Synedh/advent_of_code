console.log(
    require('fs')
        .readFileSync('input', { encoding: 'utf-8' })
        .split('\n')
        .map(value => parseInt(value))
        .reduce((result, value, i, array) => result + (value < array[i + 1]), 0)
);