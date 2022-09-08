// Remove duplicate elements from an array

let arr=[1, 2, 3, 2, 3,'1','1',1];
remove_dupicate_elements=(arr)=>{

    let unique_arr=[...new Set(arr)]
    console.log(unique_arr)
}
remove_dupicate_elements(arr)