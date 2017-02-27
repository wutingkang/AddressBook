function valiname(){
    var n=document.forms["myForm"]["name"].value;
     if("" == n || null == n){
        document.getElementById('inform').innerHTML = "姓名为空";
        return false;
    }
    else{
        document.getElementById('inform').innerHTML = "";
    }
}

function valiemailForm(){
    var x=document.forms["myForm"]["email"].value;
    var atpos=x.indexOf("@");
    var dotpos=x.lastIndexOf(".");

    if("" == x || null == x){
        document.getElementById('inform').innerHTML = "邮箱为空";
        return false;
    }
    else if (atpos<1 || dotpos<atpos+2 || dotpos+2>=x.length){
        document.getElementById('inform').innerHTML = "不是一个有效的 e-mail 地址";
        return false;
    }
    else{
        document.getElementById('inform').innerHTML = "";
    }
}

function isTelOrMobile(telephone){  
    var teleReg = /^((0\d{2,3})-)(\d{7,8})$/;  
    var mobileReg =/^1[358]\d{9}$/;   
    
    if("" == telephone || null == telephone){
        document.getElementById('inform').innerHTML = "电话号码为空";
    }
    else if(!teleReg.test(telephone) && !mobileReg.test(telephone)){  
         document.getElementById('inform').innerHTML = "电话号码格式错误";
    }
    else{
        document.getElementById('inform').innerHTML = "";
    }
} 

function valiaddress(){
    var d=document.forms["myForm"]["address"].value;
     if("" == d || null == d){
        document.getElementById('inform').innerHTML = "地址为空";
        return false;
    }
    else{
        document.getElementById('inform').innerHTML = "";
    }
}

function valiqqnumber(){
    var q=document.forms["myForm"]["QQNumber"].value;
     if("" == q || null == q){
        document.getElementById('inform').innerHTML = "QQ号码为空";
        return false;
    }
    else{
        document.getElementById('inform').innerHTML = "";
    }
}

function validateForm(){
    var temp = "";
    var name = document.forms["myForm"]["name"].value;
    var email = document.forms["myForm"]["email"].value;
    var telephone = document.forms["myForm"]["telephone"].value;
    var address = document.forms["myForm"]["address"].value;
    var QQNumber = document.forms["myForm"]["QQNumber"].value;

    if ("" == name || null == name){
        temp+="name ";    
    }
    if ("" == email || null == email){
        temp+="email ";    
    }
    if("" == telephone || null == telephone){
        temp+="telephone ";
    }
    if ("" == address || null == address){
        temp+="address ";    
    }
    if ("" == QQNumber || null == QQNumber){
        temp+="QQNumber ";    
    }

    if ("" == temp || null == temp){
        window.history.back(-1);
        return true;
    }else{
        alert(temp + "未填写");
        return false;
    }
}