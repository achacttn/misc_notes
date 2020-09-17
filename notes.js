// JavaScript notes

// Number.isInteger()

// event.target.valueAsNumber
// => returns number instead of string for event target

// required function params
let isRequired = () => {
    throw new Error('This parameter is required')
}

let greetings = ( name = isRequired(),  message="hello" ) => {
    return `${message} ${name}`;
}

// comma operator
let val = (12, 32);
// => 12 is evalulated, then 32 is assigned to val
