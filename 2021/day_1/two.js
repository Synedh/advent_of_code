console.log(
    require('fs')
        .readFileSync('input', { encoding: 'utf-8' })
        .split('\n')
        .map((_value, i, array) => parseInt(array[i]) + parseInt(array[i + 1]) + parseInt(array[i + 2]))
        .reduce((result, value, i, array) => result + (value < array[i + 1]), 0)
);