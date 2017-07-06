$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

//Comando para quando o enter for apertado no Bate-papo
$(document).keypress(function(e) {
    if(e.which == 13){
        if ($("#campo").val() !== "" && $("#checkenter").is(':checked')) {
            mandaMensagem();
        }

    };
});

function mandaMensagem(){
    var campo = $("#campo").val();
    if (campo !== ""){
        $.ajax({
            url : "send/", // the endpoint
            type : "POST", // http method
            data : {
                id : campo,
                 }, // data sent with the post request

            // handle a successful response
            success : function(json) {
                if (json != false){
                    $('#newmessage').append("<div class='col-xs-12'><p class='msg-emissor pull-right' data-toggle='tooltip' data-placement='left' title="+ json[1] +">"+ json[0] +"</p></div>");
                    goToFinal();
                    $("#campo").val('');
                    $("#alertavisualizada").html("");
                    $("#informacao").html("");
                }
                else{
                    alert("Não foi possivel enviar mensagem")
                }
                

            },

            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
               alert("deu errado");

            }
        
        });
    }


}


//Função para ir para o final do bate-papo
function goToFinal(){
    $(".nano").nanoScroller({ flash: true });
    $(".nano").nanoScroller({ scroll: 'bottom' });
}



function deletaconversa(iduser) {
    //console.log("função para saber se existe uma relaçao de seguidor");
    console.log(iduser);
    $.ajax({

        url : "/deleta_conversa/", // the endpoint
        type : "POST", // http method
        data : { 
            id : iduser,
             }, // data sent with the post request
             
        // handle a successful response
        success : function(json) {
            if(json == true){
                parent.window.document.location.href = '';
            }else{
                alert("Erro ao excluir conversa!")
            }
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
           

        }
    });
}

//Cookies globais padrões para utilização do AJAX

function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

$(".nano").nanoScroller({ scroll: 'bottom' });