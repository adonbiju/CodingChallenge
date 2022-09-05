let str="malayalam"

let split=str.split('')
let rev=split.reverse();  
let join=split.join('')

if(str==join){
    console.log(str,"is palindrome");
}else{
    console.log(str,"is not palindrome");
}

