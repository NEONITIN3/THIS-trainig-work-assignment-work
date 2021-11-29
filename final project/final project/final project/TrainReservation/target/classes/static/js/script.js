const signin__btn = document.querySelector("#signin__btn");
const signup__btn = document.querySelector("#register__btn");
const container = document.querySelector(".container");

signup__btn.addEventListener('click', () => {
    container.classList.add("signup-mode");
});

signin__btn.addEventListener('click', () => {
    container.classList.remove("signup-mode");
});

const buttons = document.querySelector('#register__btn');

buttons.addEventListener('click', function(e) {

    let x = e.clientX - e.target.offsetLeft;
    let y = e.clientY - e.target.offsetTop;

    let ripples = document.createElement('span');
    ripples.style.left = x + 'px';
    ripples.style.top = y + 'px';

    this.appendChild(ripples);

    setTimeout(() => {
        ripples.remove()
    },750);
});

// function validateform()
// {
//     var username;
//     username = document.getElementById("username").value;
//     var password;
//     password = document.getElementById("password").value;
//     if(password == "")
//     {
//         alert("Please Enter Valid Password!");
//         return false;
//     }
//     else if(username =="")
//     {
//         alert("Please Enter Valid User ID");
//         return false;
//     }
//     else if(password.length < 8)
//     {
//         alert("Password length must be atleast 8 characters");
//         return false;
//     }
//     else {  
//         alert("Password is correct");  
//      }  
// }

function validateform2()
{
    var fullname = document.getElementById("fullname").value;
    var username = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var number = document.getElementById("number").value;    
    var password = document.getElementById("password").value;

   
    if(isNaN(number))
    {
        alert("Please Enter Valid Phone Number!");
        return false;
    }
    // else
    // {
    //     alert("User created successfully");  
    // }
}