const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

// 1. Driver 🚗
// 2. Presenter 👩‍💻
// 3. Navigator 🧭

// take 5-7 mins to write the pseudocode here:

// create the function and decide what params it needs and what it will return
function join(arr, separator) {
    var result=""
    for(var i=0; i<arr.length;i++){
        if(i==arr.length - 1) {
            // console.log(arr[i]);
            result+=arr[i]+separator
        } else {
            // console.log(arr[i]);
            result+=arr[i]+separator
        }
    }
    return result
}

console.log(join(arr1,separator1))
