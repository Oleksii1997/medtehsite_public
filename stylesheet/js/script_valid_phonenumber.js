$(document).ready(function(){  
	$(".tel_input").on("input",function(e){
		e.preventDefault();
		phone_number=$(e.target).val();
		console.log(phone_number.length)
		if((/^[0][1-9][0-9]+$/.test(phone_number))&&(phone_number.length==10)){
			console.log("true");
			$('.button_registration').attr("disabled", false);
			$('.button_make_registration').removeClass("button_disabled");
			$('.valid_phone').addClass("valid_phone_hidden");
		}
		else{
			$('.button_registration').attr("disabled", true);
			$('.button_make_registration').addClass("button_disabled");
			$('.valid_phone').removeClass("valid_phone_hidden");
			console.log("false");
		}
	});
});