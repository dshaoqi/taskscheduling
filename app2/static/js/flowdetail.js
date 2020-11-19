function getFlowStatus(){
    $.post("/flowstatus",{flowid:flowid},
               function(data,status){
                   if(data=='ok'){
                        console.log('get ok');
                   }
                   else{}
                }
}
function reminder(){
    //alert("是否确定执行flow!");
    var c = confirm("执行flow请点击确认，否则点击取消");
    if(c==true){
        var flowid = document.getElementById("flowid");
        $.post("/flowcommit",{flowid:flowid},
               function(data,status){
                   if(data=='ok'){
                        console.log('get ok');
                        setInterval(function(){ getFlowStatus() },1);
                   }
                   else{
                        console.log('get no,please check the flow status');
                   }
                }
        );
    }
    else{
        alert("已取消执行flow的命令");
    }
}
