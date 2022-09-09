$("#frm").submit(function(e){
	if(fileCheck()) {
		loading();
    }else{
        return false;
        }
});

function loading() {
    $("#process").after('<div id="load"><img src="/static/images/loading_icon.gif"></div>');
}

function fileCheck(){
    let fileCheck = document.getElementById("imgUpload").value;
    if(!fileCheck){
        return false;
    }
}

function readURL(input) {
    if (input.files && input.files[0]) {
        let reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById('preview').src = e.target.result;
            document.getElementById('preview').style.width = "350px";
            document.getElementById('preview').style.height = "350px";
        };
        reader.readAsDataURL(input.files[0]);
    } else {
        document.getElementById('preview').src = "";
    }
}


