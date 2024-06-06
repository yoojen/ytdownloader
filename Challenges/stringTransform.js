/**
 * Helper function to reverse string
 * @param {String} input - Input string to be reversed
 * @returns {String} - Returns reversed string
 */
function reverseString(input) {
    let reversed = ""
    for (let i = input.length - 1; i >=0; i--) {
        reversed += input[i]
    }
    return reversed.replace(/ /g, '');
}


/**
 * Find unicode for each characters in string
 * @param {String} input 
 * @returns {String} - Returns ASCII codes corresponding to input text 
 */
function charToAsciiUnicode(input) {
    let asciiCodes = ""
    for (let i = 1; i < input.length; i++) {
       asciiCodes += `${input.charCodeAt(i)} `;
    }
    return asciiCodes;
}


/**
 * Actual string transformer
 * @param {String} string - The input to be processed
 * @returns {String} Returns new transformed version of input
 */
function stringTransformation(string) {
    const stringLength = string.length

    if ((stringLength % 3 == 0) && (stringLength % 5 == 0)) {
        const reversed = reverseString(string);
        return reversed
    }
    if (stringLength % 3 == 0) {
        const reversed = reverseString(string)
        return reversed
    }
    if (stringLength % 5 == 0) {
        const charAsciiCodes = charToAsciiUnicode(string)
        return charAsciiCodes
    }
}
