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