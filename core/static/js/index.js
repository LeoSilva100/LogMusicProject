$('#sign').submit(function() {
    var form = $(this);
    $('.t1').addClass("semfunc");
    $.post(form.attr('action'), form.serialize(), function(retorno) {
        
        var iName = $('#aunome').val()
        var iPass = $('#ausenha').val()
        if (iName == '' || iPass == '') {
            $('.t1').removeClass("semfunc");
        } else{
            $('.pre1').removeClass("semfunc");
            $.ajax({
                url : "/autentica/",
                type : "POST",
                data : { 
                    username : iName,
                    password : iPass,
                     },

                success : function(json) {
                    if (json == true) {
                        parent.window.document.location.href = '/';
                    } else {
                        $('.pre1').addClass("semfunc");
                        $('.t1').removeClass("semfunc");                        
                    }            
                },

                error : function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText);
                   $('.pre1').addClass("semfunc");
                   $('.t1').removeClass("semfunc");

                }
            }); 
        }
    });
    return false;
});

$('#register').submit(function() {
    var form = $(this);
    $('.t1').addClass("semfunc");
    $.post(form.attr('action'), form.serialize(), function(retorno) {
        
        var iName = $('#nomer').val();
        var iEmail = $('#emailr').val();
        var iSenha = $('#passwordr').val();

        if (iName == '' || iEmail == '' || iSenha == '') {
            $('.t2').removeClass("semfunc");
        } else{
            $('.pre2').removeClass("semfunc");
            $.ajax({
                url : "/registra/",
                type : "POST",
                data : { 
                    username : iName,
                    email : iEmail,
                    password : iSenha,
                     },

                success : function(json) {
                    console.log("Resultado do processamento: "+json);
                    if (json == true) {
                        parent.window.document.location.href = '/';
                    } else {
                        $('.pre2').addClass("semfunc");
                        $('.t2').removeClass("semfunc");
                        
                    }            
                },

                error : function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText);
                   $('.pre2').addClass("semfunc");
                   $('.t2').removeClass("semfunc");

                }
            }); 
        }
    });
    return false;
});

function delete_account(){
    $.ajax({
        url : "/deletaconta/",
        type : "GET",
        
        success : function(json) {
            if (json == true) {
                parent.window.document.location.href = '/';
            } else {
                alert("Something went wrong....");
            }            
        },

        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
           alert("Something went wrong.")

        }
    }); 
       
}

var form = new FormData();

function addMusicProfile(){
    console.log("apertado");
    var age = $("#age").val();
    var city = $("#city").val();
    var instrument = $("#instrument").val();
    var state = $("#state").val();
    var style = $("#style").val();
    var adress = $("#adress").val();
    var phone = $("#phone").val();
    var face = $("#face").val();
    var twitter = $("#twitter").val();
    var insta = $("#insta").val();
    var video = $("#video").val();

    console.log(age);
    console.log(city);
    console.log(instrument);
    console.log(state);
    console.log(style);
    console.log(adress);
    console.log(phone);
    console.log(face);
    console.log(twitter);
    console.log(insta);

    
    form.append('age', age);
    form.append('city', city);
    form.append('instrument', instrument);
    form.append('state', state);
    form.append('style', style);
    form.append('adress', adress);
    form.append('phone', phone); 
    form.append('face', face); 
    form.append('twitter', twitter); 
    form.append('insta', insta); 
    form.append('video', video);   

    
    $.ajax({
        url : "/postProfile/",
        type : "POST",
        data : form,
        processData: false,
        contentType: false,

        success : function(json) {
            console.log("Resultado do processamento: "+json);
            if (json == true) {
                parent.window.document.location.href = '/';
            } else {
                Materialize.toast('Algo de errado aconteceu. Verifique os campos...', 4000);
                //$('.loadadd').addClass("semfunc");
            }            
        },

        beforeSend: function(){
            var $toastContent = $('<span>Salvando, aguarde...</span>');
            Materialize.toast($toastContent, 7000);
        },

        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
           Materialize.toast('Erro: '+xhr.status, 4000);
           //$('.loadadd').addClass("semfunc");

        }
    }); 
        

    return false;
    
    
    
}


var formProfile = new FormData();
    $('#profile').change(function (event) {
        console.log("mudou a foto de perfil");
        formProfile.append('profile', event.target.files[0]); // para apenas 1 arquivo
        //var nameee = event.target.files[0].content; // para capturar o nome do arquivo com sua extenção
    });
    $('#cover').change(function (event) {
        formProfile.append('cover', event.target.files[0]); // para apenas 1 arquivo
        //var nameee = event.target.files[0].content; // para capturar o nome do arquivo com sua extenção
    });

function editProfile(){
    console.log("apertado");
    var username = $("#username").val();
    var email= $("#email").val();

    
    formProfile.append('username', username);
    formProfile.append('email', email); 

    
    $.ajax({
        url : "/edit_profile/",
        type : "POST",
        data : formProfile,
        processData: false,
        contentType: false,



        success : function(json) {
            console.log("Resultado do processamento: "+json);
            if (json == true) {
                parent.window.document.location.href = '/';
            } else {
                Materialize.toast('Complete todos os campos', 4000);
                //$('.loadadd').addClass("semfunc");
            }            
        },

        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
           Materialize.toast('Erro: '+xhr.status, 4000);
           //$('.loadadd').addClass("semfunc");

        }
    }); 
        

    return false;

    
    
}

function delete_chat(iduser) {
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

function mandaMensagem(campo){
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
                }
                else{
                    Materialize.toast('Erro ao enviar mensagem', 4000);
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

$('#fa').submit(function() {
    Materialize.toast('Enviando...', 4000);
    console.log();
    var form = $(this);
    $.post(form.attr('action'), form.serialize(), function(retorno) {
        if ($("#campo").val() !== "") {
            console.log($("#campo").val());
            mandaMensagem($("#campo").val());
        }
        
          //window.location.replace("/search="+ $("#pesquisa").val() +"");
    });
    Materialize.toast('Mensagem enviada', 4000);
    $('#warn').html("<a class='waves-effect waves-light btn center-align' href=''><i class='material-icons right'>loop</i>Atualizar mensagens</a>");
    return false;

});

$('#f').submit(function() {
    console.log();
    var form = $(this);
    $.post(form.attr('action'), form.serialize(), function(retorno) {

    });
    return false;
});

function search_users(message){
    console.log("Evento para adicionar mensagem");
    //$('.loadadd').removeClass("semfunc");
    
    $.ajax({
        url : "/search_users/",
        type : "POST",
        data : { 
            message : message
             },
        success : function(json) {
            $('.resultData').html("");
            $('.resultTxt').html("");
            
            if (json != false) {

                console.log("Resultado do processamento: "+json);
                  $('.resultTxt').html(
                '<h6>Resultados para <i>'+ message +'</i>:<h6>');
                for (var i = json.length - 1; i >= 0; i--) {
                    $('.resultData').append("<li class='collection-item'><div><a href='/profile/"+json[i].username+"'><b>"+ json[i].username +"</b><span style='color: black;''> (" + json[i].email +")</span></a><a id='idsuserlink"+json[i].pk+"' href='/inbox/message/"+json[i].pk+"'  class='secondary-content'><i class='material-icons idsuser"+json[i].pk+"'>message</i></a></div></li>");
                    console.log(json[i].username);
                }
                //parent.window.document.location.href = '';
            } else {
                Materialize.toast('Nenhum resultado', 4000);
                //$('.loadadd').addClass("semfunc");
            }            
        },

        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
           Materialize.toast('Erro: '+xhr.status, 4000);
           //$('.loadadd').addClass("semfunc");

        }
    }); 
    return false;
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

$('#slide-contatos, #slide-seguindo').slick({
  dots: false,
  infinite: false,
  speed: 300,
  slidesToShow: 5,
  slidesToScroll: 2,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
        dots: false
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
});
