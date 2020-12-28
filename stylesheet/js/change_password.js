$(document).ready(function(){
 
//Форма зміни паролю 

  	$('#view_password3').click(function(){ //view password 
        var type = $('#password3').attr('type') == "text" ? "password" : 'text';
        c = $(this).text() == "Приховати пароль" ? "Показать пароль" : "Приховати пароль";
        $(this).text(c);
        $('#password3').prop('type', type);
    });
    $('#view_password4').click(function(){ 
        var type = $('#password4').attr('type') == "text" ? "password" : 'text';
        c = $(this).text() == "Приховати пароль" ? "Показать пароль" : "Приховати пароль";
        $(this).text(c);
        $('#password4').prop('type', type);
    });

    $('#view_password5').click(function(){ 
        var type = $('#password5').attr('type') == "text" ? "password" : 'text';
        c = $(this).text() == "Приховати пароль" ? "Показать пароль" : "Приховати пароль";
        $(this).text(c);
        $('#password5').prop('type', type);
    });

    var valid_password_1 = false;
    var valid_password_2 = false;

    $(".new_password").on("input",function(e){
		e.preventDefault();
		var new_password = $('#password4').val();
		var new_password_repeat = $('#password5').val();

		if (new_password.length > 0) {//перевірка паролів на "складність"
			if((new_password.match(/[A-Z]/))&&(new_password.match(/[a-z]/))&&(new_password.match(/[0-9]/))&&(new_password.length >= 8)){
				$('.new_custumer_password_input_4').removeClass('invalid').addClass('valid');
				$('.reliable_new_password_4').addClass('valid_hidden');
				valid_password_1 = true;
			}
			else{
				$('.new_custumer_password_input_4').removeClass('valid').addClass('invalid');
				$('.reliable_new_password_4').removeClass('valid_hidden');
				valid_password_1 = false;
			}
		}
		else{
			$('.new_custumer_password_input_4').removeClass('valid').removeClass('invalid');
			$('.reliable_new_password_4').addClass('valid_hidden');
			valid_password_1 = false;
		}
		if (new_password_repeat.length > 0) {
			if((new_password_repeat.match(/[A-Z]/))&&(new_password_repeat.match(/[a-z]/))&&(new_password_repeat.match(/[0-9]/))&&(new_password_repeat.length >= 8)){
				$('.new_custumer_password_input_5').removeClass('invalid').addClass('valid');
				$('.reliable_new_password_5').addClass('valid_hidden');
				valid_password_2 = true;
			}
			else{
				$('.new_custumer_password_input_5').removeClass('valid').addClass('invalid');
				$('.reliable_new_password_5').removeClass('valid_hidden');
				valid_password_2 = false;
			}
		}
		else{
			$('.new_custumer_password_input_5').removeClass('valid').removeClass('invalid');
			$('.reliable_new_password_5').addClass('valid_hidden');
			valid_password_2 = false;
		}

		if((new_password.length > 0)&&(new_password_repeat.length > 0)){//Перевірка паролів на співпадіння
			if (new_password==new_password_repeat) {
				if ((new_password.length >= 8)&&(valid_password_1)) {
					$('.new_custumer_password_input_4').addClass('valid').removeClass('invalid');
					$('.new_custumer_password_input_5').addClass('valid').removeClass('invalid');
				}
				$('.valid_new_password').addClass('valid_hidden');
			}
			else{
				$('.new_custumer_password_input_4').removeClass('valid').addClass('invalid');
				$('.new_custumer_password_input_5').removeClass('valid').addClass('invalid');
				$('.valid_new_password').removeClass('valid_hidden');
			}
		}
		else{
			$('.valid_new_password').addClass('valid_hidden');
		}
	});
	$(".password").on("input",function(e){
		$('.custumer_password_input').removeClass('valid').removeClass('invalid');
		$('.valid_old_password').addClass('valid_hidden');
	});

	var form_change = $('#change_password');//for change password
	form_change.on('submit',function(e){          
		e.preventDefault();  
		console.log("submit");              
		var data = {};
		var csrf_token = $('#password_recovery [name="csrfmiddlewaretoken"]').val();
		data["csrfmiddlewaretoken"] = csrf_token;
		data["username"] = $('#phone_number').val();
		data["old_password"] = $('#password3').val();
		data["new_password"] = $('#password4').val();
		data["repeat_new_password"] = $('#password5').val();
		data["valid_password_1"] = valid_password_1;
		data["valid_password_2"] = valid_password_2;
		var url = form_change.attr("action");
		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			success: function(data){
				console.log("ok");
				console.log(data);
				if (data.username_valid) {
					$('.custumer_username_input').addClass('valid').removeClass('invalid');
					$('.valid_user').addClass('valid_hidden');
					if (data.old_password_valid) {
						$('.custumer_password_input').addClass('valid').removeClass('invalid');
						$('.valid_old_password').addClass('valid_hidden');
						if (data.same_password) {
							$('.valid_new_password').addClass('valid_hidden');
							if (data.password_change) {
								$('.reliable_new_password').addClass('valid_hidden');
								$('.custumer_password_input_4, .custumer_password_input_5').addClass('valid').removeClass('invalid');
								$('.success_change_password').removeClass('valid_hidden');
								$('body,html').animate({scrollTop: 0}, 400); 
							}
						}
						else{
							$('.valid_new_password').removeClass('valid_hidden');
							$('.reliable_new_password').addClass('valid_hidden');
							$('.custumer_password_input_4, .custumer_password_input_5').removeClass('valid').addClass('invalid');
						}
					}
					else{
						$('.custumer_password_input').removeClass('valid').addClass('invalid');
						$('.valid_old_password').removeClass('valid_hidden');
					}
				}
				else{
					$('.custumer_username_input').removeClass('valid').addClass('invalid');
					$('.valid_user').removeClass('valid_hidden');
					$('.custumer_password_input').removeClass('valid').removeClass('invalid');
					$('.valid_old_password').addClass('valid_hidden');
				}
			},
			error: function(data){
				console.log("error");
			}
		})
	})
	
});
/*

	
	function sendContactInfo(){
		var form_contact = $('#contact_form');             
		var data = {};
		var csrf_token = $('#contact_form [name="csrfmiddlewaretoken"]').val();
		data["csrfmiddlewaretoken"] = csrf_token;
		var name_client = $('.name_client_input').val();
		var phone_client = $('.phone_client_input').val();
		var email_client = $('.email_client_input').val();
		data["name_client"] = name_client;
		data["phone_client"] = phone_client;
		data["email_client"] = email_client;
		var url = form_contact.attr("action");
		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			success: function(data){
				console.log("ok");
				console.log(data);
				if (data.send_status==true){
					$('.name_client_input').val('');
					$('.phone_client_input').val('');
					$('.email_client_input').val('');
					$('.contact_form').addClass("error_name_hidden");
					$('.success_massage').removeClass("success_logo_hidden");
				}
			},
			error: function(data){
				console.log("error");
				$('.name_client_input').val('');
				$('.phone_client_input').val('');
				$('.email_client_input').val('');
				$('.contact_form').addClass("error_name_hidden");
				$('.no_success_massage').removeClass("success_logo_hidden");
			}
		})
	}
	//функція перевірки валідності e-mail
	function isValidEmailAddress(emailAddress) {
    	var pattern = new RegExp(/^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i);
    	return pattern.test(emailAddress);
    }
	$(".need_help_button").click(function(e){
		e.preventDefault();

		var name_client = $('.name_client_input').val()
		if (name_client.length==0) {
			$('.name_client').removeClass("valid_input");
			$('.name_client').addClass("error_input");
			$('.error_name').removeClass("error_name_hidden");
			var valid_name = false;
		}
		else{
			$('.name_client').removeClass("error_input");
			$('.error_name').addClass("error_name_hidden");
			$('.name_client').addClass("valid_input");
			var valid_name = true;
		}

		var phone_number = $('.phone_client_input').val()
		if((/^[0][1-9][0-9]+$/.test(phone_number))&&(phone_number.length==10)){
			$('.phone_client').removeClass("error_input");
			$('.error_phone').addClass("error_name_hidden");
			$('.phone_client').addClass("valid_input");
			var valid_phone = true;
		}
		else{
			$('.phone_client').removeClass("valid_input");
			$('.phone_client').addClass("error_input");
			$('.error_phone').removeClass("error_name_hidden");
			var valid_phone = false;
		}

		var email_address = $('.email_client_input').val()
		if(isValidEmailAddress(email_address)){
			$('.email_client').removeClass("error_input");
			$('.error_email').addClass("error_name_hidden");
			$('.email_client').addClass("valid_input");
			var valid_email = true;
		}
		else{
			$('.email_client').removeClass("valid_input");
			$('.email_client').addClass("error_input");
			$('.error_email').removeClass("error_name_hidden");
			var valid_email = false;
		}

		if ((valid_name==true)&&(valid_email==true)&&(valid_phone==true)) {
			sendContactInfo();
		}
	});

*/