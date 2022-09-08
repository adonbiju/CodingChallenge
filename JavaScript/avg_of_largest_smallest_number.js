// Find the average of largest and smallest numbers in an unsorted integer array?
// Eg. [1, 4, 3, 2] => average = (1+4)/2 = 2.5[1, 4, 3, 4] => average = (1+4+4)/3 = 3


arr=[1, 4, 3, 4]

function avg_of_largest_smallest_number(arr){
    largest_number=Math.max.apply(null,arr)
    smallest_number=Math.min.apply(null,arr)
    let largest_number_count=0
    let smallest_number_count=0
    console.log("largest number is",largest_number)
    console.log("smallest number is ",smallest_number)
     for(i=0;i<arr.length;i++){
        if (arr[i]==largest_number){
            largest_number_count=largest_number_count+1
        }
     }
     for(i=0;i<arr.length;i++){
        if (arr[i]==smallest_number){
            smallest_number_count=smallest_number_count+1
        }
     }
    
     let avg=parseFloat(((largest_number_count*largest_number)+(smallest_number_count*smallest_number))/(largest_number_count+smallest_number_count))
     console.log("average is",avg)
     
}
avg_of_largest_smallest_number(arr)

