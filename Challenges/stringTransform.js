/**
 * reverString: Helper function to reverse string
 * input: string to be reversed
 * Return: String
 */
function reverseString(input) {
    for (let i = input.length; i < 0; i--) {
        console.log(input[i])
    }
}
reverseString("eugene");
/**
 * stringTransformation: Transform string based on divisibility
 * string: Input to be processed
 * Return: Boolean 
 */
function stringTransformation(string) {
    const stringLength = string.length

    if ((stringLength % 3 == 0) && (stringLength % 5)) {
        console.log("divisible by btth 3 and 5")
    }
    if (stringLength % 3 == 0) {
        console.log("divisible by 3")
    }
    if (stringLength % 5 == 0) {
        console.log("divisible by 3")
    }
}