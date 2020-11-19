function reminder(){
    //alert("是否确定执行flow!");
    var c = confirm("执行flow请点击确认，否则点击取消");
    if(c==true){
        var tab = document.getElementById("fmlist");
        for(var i=1,rows=tab.rows.length;i<rows;i++){
            var len = tab.rows[i].cells.length;
            var  methodid = tab.rows[i].cells[len-1].innerHTML;
            console.log(tab.rows[i].cells[0].innerHTML)
            $.post("/flowcommit",{methodid:methodid},
                function(data,status){
                    if(data=='ok'){
                        console.log('get ok');
                    }
                    else{}
                }
            );
        }
    }
    else{
        alert("已取消执行flow的命令");
    }
}
