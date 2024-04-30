function cloneArray(array){
    return [...array]
}

function sum(a, b){
    return a +b
}

test('adds 2 numbers', () => {
    expect(
        sum(1,2)
    ).toBe(3)
})

test('properly clones array', () => {
    const array = [1,2,3]
    expect(
        cloneArray(array)
    ).toEqual(array)
    expect(
        cloneArray(array)
    ).not.toBe(array)
})

// jest --coverage will show overall coverage of tests