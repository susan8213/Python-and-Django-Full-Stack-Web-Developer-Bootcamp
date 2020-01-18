var firstName = prompt("First Name: ");
var lastName = prompt("Last Name: ");
var age = prompt("Age: ");
var height = prompt("Height (cm): ");
var pet = prompt("Pet Name: ");

var pass1 = (firstName[0] === lastName[0]);
var pass2 = (age > 20 && age < 30);
var pass3 = (height >= 170);
var pass4 = (pet[pet.length-1] === "y");
var isSpy = (pass1 && pass2 && pass3 && pass4);

if(isSpy){
    console.log("YOU ARE THE SPY !!!!!");
}