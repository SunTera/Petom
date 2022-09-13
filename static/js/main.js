function loading() {
    $("#process").after('<div id="load"><img src="/static/images/loading_icon.gif"></div>');
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


