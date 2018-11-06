$(document).ready(function(){
    $('#error').hide()
    $('#submit').click(function(){
        var title = $('#title').val()
        var url = $('#long_url').val()
        url_info = {'values':[title,url]}
        if ((title && url) != ''){
            if ((title.length > 2) && (title.length < 20 )){
                if (url.length > 15) {
                    var dir = '/shorten'
                    var server = 'http://127.0.0.1:5000'
                    $.post(server+dir,JSON.stringify(url_info),function(response){
                        alert(JSON.stringify(response))
                        console.log(response)
                    })
                }else{
                    $('#error').text("Url must be higher than 15 characters long!");
                    $('#error').show(300);
                }  
            }else{
                $('#error').text("Title must be between 3 and 20 characters long!");
                $('#error').show(300);
            }
        }else{
            $('#error').show(300);
        }
    });
});
/* ({
                        type: "POST",
                        url:server+dir,
                        data: JSON.stringify(url_info),
                        data_type: 'json'
                    }).done(function(result){
                        console.log(result)
                    }) */