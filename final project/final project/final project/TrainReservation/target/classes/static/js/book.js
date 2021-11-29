function verify()
{
    var age;
    var name;
    name = document.getElementById("name").value;
    age = Number(document.getElementById("age").value);

    
    if(isNaN(age))
    {
        alert("age Input not valid!");
        return false;
    }
    else if(age<0)
    {
        alert("you have entered an invalid age Number");
        return false;
    }
    else if(age>0 && age<6)
    {
        alert("you don't need to buy ticket for child having age less then 5");
        return false;
    }

}
