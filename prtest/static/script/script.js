function clickfun()
{
    errors = [];
    var name = document.getElementById("name").value;
    var mail = document.getElementById("email").value;
    var gen = document.getElementById("gender").value;
    var num=document.getElementById("num").value;
    var pnum=document.getElementById("pnum").value;
    if(num.toString().length!=10)
        {
            errors.push("Number doesn't follow properties of a number");
        }
        if(pnum.toString().length!=10)
            {
            errors.push("Parent Nunber doesn't follow properties of a number");
        }
        
        var p = document.getElementById("passwd").value;
            if (p.length < 8) {
                errors.push("Your password must be at least 8 characters"); 
            }
            if (p.search(/[a-z]/i) < 0) {
                errors.push("Your password must contain at least one letter.");
            }
            if (p.search(/[0-9]/) < 0) {
                errors.push("Your password must contain at least one digit."); 
            }
            if (p.search(/[a-z]/) < 0) {
                errors.push("Your password must contain at least one lowercase letter.");
            }
            if (p.search(/[A-Z]/) < 0)
            {
                errors.push("Your password must contain at least one uppercase letter.");
            }
            var p2=document.getElementById("passwd1").value;
            if(p!=p2)
            {
                errors.push("Passwords are not same");
            }
    if (errors.length > 0) {
            alert(errors.join("\n"));
            return false;
        }
        else{
            return true;
        }
    return true;
}