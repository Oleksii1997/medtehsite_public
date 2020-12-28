$(document).ready(function(){  
	$('.add_email_button').on('click', function(e){   
		e.preventDefault();
		email_address=$(".email_input").val();
		if(email_address.length != 0){
			$('.valid_email_notlength').addClass('form_valid_field_hidden');
			if(isValidEmailAddress(email_address)){
				$('.valid_email_field').addClass('form_valid_field_hidden');
				$('.email_advertis').removeClass('email_advertis_input_error');
				$('.email_advertis').removeClass('email_advertis_input_valid');
				$('.list_email_send').removeClass('list_email_send_hidden');
				$('.make_email_input').append('<div class="checkbox_input_box">' +
														'<input type="checkbox" name="list_add_email" class="checkbox" checked="checked"'+ email_address + '" id="' + email_address + '" value="'+ email_address +'">' +
														'<label for="' + email_address + '">'+ email_address + '</label>' +
												'</div>');
				$(".email_input").val(" ");
			}										
			else{
				$('.valid_email_field').removeClass('form_valid_field_hidden');
				$('.email_advertis').removeClass('email_advertis_input_valid');
				$('.email_advertis').addClass('email_advertis_input_error');
			}
		}
		else{
			$('.valid_email_notlength').removeClass('form_valid_field_hidden');
			$('.email_advertis').removeClass('email_advertis_input_valid');
			$('.email_advertis').addClass('email_advertis_input_error');
		}
	});

	//функція перевірки валідності e-mail
	function isValidEmailAddress(emailAddress) {
    	var pattern = new RegExp(/^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i);
    	return pattern.test(emailAddress);
    }

  	//перевірка валідації e-mail при введенні адреси
	$(".email_input").on("input",function(e){
		e.preventDefault();
		email_address=$(e.target).val();
		if(email_address.length != 0){
			$('.valid_email_field').addClass('form_valid_field_hidden');
			$('.valid_email_notlength').addClass('form_valid_field_hidden');
			if(isValidEmailAddress(email_address)){
				$('.email_advertis').removeClass('email_advertis_input_error');
				$('.email_advertis').addClass('email_advertis_input_valid');
			}
			else{
				$('.email_advertis').removeClass('email_advertis_input_valid');
				$('.email_advertis').addClass('email_advertis_input_error');
			}
		}
		else{
			$('.email_advertis').removeClass('email_advertis_input_valid');
			$('.email_advertis').removeClass('email_advertis_input_error');
		}
	});

	$(".checked_all").change(function(e){//Вкл/Викл всі checkbox одним
		e.preventDefault();
		if ($('.checked_all').is(':checked')) {
			$('.checkbox_advertis_email').prop('checked', true);
		}
		else{
			$('.checkbox_advertis_email').prop('checked', false);
		}
	});
});