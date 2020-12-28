$(document).ready(function(){
  $("#image_carousel").owlCarousel({
  	items:1,
  	loop:true,
  	//dots:false,
    nav:true,
  	autoplay:true,
    autoplayTimeout:5000,
    autoplayHoverPause:true
  });
//Контактна форма на сторінці ремонтів "Замовити консультацію"
	
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
});