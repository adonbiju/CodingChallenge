// JavaScript Array map()---------------------------------------------------------------------
const numbers = [4, 9, 16, 25];
const newArr = numbers.map(Math.sqrt)
console.log(newArr)

// [ 2, 3, 4, 5 ]


const numbers2 = [4, 9, 16, 25];
const newArr2=numbers2.map((id)=>{return id*10})
console.log(newArr2)

// [ 40, 90, 160, 250 ]

const persons = [
    {firstname : "Adon", lastname: "Biju"},
    {firstname : "Jion", lastname: "Biju"},
    {firstname : "Ashin", lastname: "KJ"}
  ];
const fullname=persons.map((name)=> {return[name.firstname,name.lastname].join(" ")})
console.log(fullname)

// [ 'Adon Biju', 'Jion Biju', 'Ashin KJ' ]

// JavaScript Array map()---------------------------------------------------------------------END


// JavaScript Array filter()---------------------------------------------------------------------
const ages = [32, 33, 16, 40];
const result = ages.filter((age)=>{return age>30});
console.log(result)

// [ 32, 33, 40 ]

const ages2 = [32, 33, 16, 40];
const delAge=40
const result2 = ages.filter((age)=>{return age!=delAge});
console.log(result2)

// [ 32, 33, 16 ]

// JavaScript Array filter()-------------------------------------------------------------------END


// JavaScript Array reduce()----------------------------------------------------------------------

const numbers3 = [175, 50, 25];
const result3=numbers3.reduce((total,num)=>{return total-num})
console.log(result3)
//substracting the numbers in the array, starting from the left:
//175-50-25
//100

//sum of the elements in the
const numbers4 = [175, 50, 25];
const result4=numbers4.reduce((total,num)=>{ return total+num})
console.log(result4)
//total==175 num=50
//total==175+50  num=25
//total==225+25==>250

//adding the numbers in the array, starting from the left:
//175+50+25
//250

// JavaScript Array reduce()--------------------------------------------------------------------END