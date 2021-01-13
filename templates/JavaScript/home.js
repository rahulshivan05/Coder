// console.log('hello Rahul');

// variables

var b = 'Mac';
// console.log(b);

var sumNumber = 45+64;
// console.log(sumNumber);

document.getElementById('someText').innerHTML = 'Hello JS';


// var age = prompt('What is Your age');
// document.getElementById('age').innerHTML = age;


// Numbers in JavaScript


// incrementing number 
var num1 = 5.7;
num1++ // = num1 + 1; 
// console.log(num1);


// decrementing number
num1--;
// console.log(num1);

// incrementing or decrementing by any number you want
num1 += 10;
// console.log(num1);


// functions

function age() {
	// var age = prompt('Enter Your age?');
	document.getElementById('age').innerHTML = 'Your age is: ' + age;
}



function greeting(yourName) {
	
	var result = 'Hello' + ' ' + yourName; // string concatenation
	console.log(result); 
}
// var name = prompt('Enter Your name?');

// greeting(name);

function sumNumbers(num1 , num2) {
	var result = num1 + num2;
	console.log(result);
}

// sumNumbers('Hello ', 'Rahul');



var num = 0;

// while (false){
// 	num += 1;
// 	console.log(num);
// }


// FOR LOOP

for(let num = 0; num <= 100; num++) {
	// console.log(num);
}

// Data Types

let yourAge = 18; // numbeer
let yourName = 'Bob'; // string
let name = {first: 'Jana', last: 'Doe'}; // object
let truth = false; // boolean
let groceries = ['apple', 'banana', 'orange']; // aray
let random; // undefined
let nothing; // value null


// String in Javascript (common method)

let fruit = 'banana, apple, orange, blackberry';
let moreFruits = 'banana\napple'; // new line
// console.log(moreFruits); 
console.log(fruit.length);
console.log(fruit.indexOf('nan'));
console.log(fruit.slice(2, 6));
console.log(fruit.replace('ban', '123'));
console.log(fruit.toUpperCase(fruit));
console.log(fruit.toLowerCase(fruit));
console.log(fruit.charAt(2));
console.log(fruit[2]);
console.log(fruit.split(',')); // splict by a comma
console.log(fruit.split('')); // splict by character


// Array

let fruits = ['banana', 'apple', 'orange', 'pineapples'];
fruits = new Array('banana', 'apple', 'orange', 'pineapples');

console.log(fruits[2]); // access the value at index 2nd.

fruits[0] = 'pear'; // asign the value at banana
// console.log(fruits);

for(let i = 0; i < fruits.length; i++){
	console.log(fruits[1]);
}


// Array common methods

console.log('to String ' ,fruits.toString());
console.log(fruits.join(' - '));
console.log(fruits.pop(' * '));
console.log(fruits.pop(), fruits); // remove last item
console.log(fruits.push('blackberries'), fruits); // apends item.
console.log(fruits[2]);

fruits[fruits.length] = 'new Fruits';
console.log(fruits);
fruits.shift(); // remove first element
console.log(fruits)
fruits.unshift('kiwi');
console.log(fruits); // add first element

let vegatable = ['asparagus', 'tomato', 'broccoli'];
let allGroceries = fruits.concat(vegatable);
console.log(allGroceries);
console.log(allGroceries.slice(1,4));
console.log(allGroceries.reverse());


let someNumbers = [5, 10, 2, 25, 3, 255, 1, 85, 91, 56, 79, 20];
console.log(someNumbers.sort(function(a, b) {return a-b})); // sorted in ascending order
console.log(someNumbers.sort(function(a, b) {return b-a})); // sorted in descending order

let emptyArray = new Array();
for(let num = 0; num < 10; num++) {
	emptyArray.push(num);
}
console.log(emptyArray);

let student = {first: 'Rahul', 
	last: 'Kumar',
	studentInfo: function (){
		return this.first + '\n' + this.last + '\n';
	}
};

console.log(student.first);
console.log(student.studentInfo());

// Contionals, controls flows (if else)
// 18-35 is my target demographic
// && for and
// || for OR 

var age = 19;

if ((age >= 18) && (age <= 35)) {
	status = 'target demo';
	// console.log(status);
}else{
	status = 'not my audience';
	// console.log(status);
}


// Switch statements
// differentiate b/w weekday vs weekend

// day 6--> Saturday
switch (2) {
	case 0:
		text = 'weekend';
		break;
	case 5:
		text = 'weekend';
		break;
	case 6:
		text = 'weekend';
		break;
	default:
		text = 'weekday';		
}
console.log(text);