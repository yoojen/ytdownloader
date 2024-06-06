/**
 * Check if array has contigous subarray
 * @param {Array} arr - Array of integers
 * @param {number} target - Target sum
 * @returns {boolean} Returns true when subarray found, otherwise returns false
 */
function findContigousSubArray(arr, target) {
    let currentSum = 0
    let i = 0
    
    for(let j = 0; j < arr.length; j++){
        currentSum += arr[j]
        
        while (currentSum > target && i <= j){
            currentSum -= arr[i]
            i += 1
        }

        if (currentSum == target){
            return true
        }
    }
    
    return false
}

console.log(findContigousSubArray(arr=[1, 2, 3, 4 ,5], target=9))