function reminder(){
    //alert("是否确定执行flow!");
    var c = confirm("执行flow请点击确认，否则点击取消")
    if(c==true){
        alert("收到执行flow的命令");
    }
    else{
        alert("已取消执行flow的命令");
    }
}
