let n=123
let rev=0
let digit
let temp=n

while(n!=0){
    digit=n%10
    rev=parseInt((rev*10)+digit)
    n=parseInt(n/10)
}

if(rev===temp){
    console.log(temp,"is palindrome");
}else{
    console.log(temp,"is  not palindrome");
}
