
$(document).ready(function(){               //it is standart wrapper in jQuery ( code run after load all html code )
	var form = $('#form_buying_product');   //select the form by id
	console.log(form);                      //"print" the form

	function busketUpdating(product_id, number, is_delete, add_item, minus_item){
		var data = {};//дані які ми відправляємо
		data.product_id = product_id;
		data.number = number
		/*var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
		data["csrfmiddlewaretoken"] = csrf_token;*/
		var csrf_token = $('#csrf_token_form [name="csrfmiddlewaretoken"]').val();
		data["csrfmiddlewaretoken"] = csrf_token;

		if (is_delete){
			data["is_delete"] = true;
			form = $('#csrf_token_form');
		}
		if(add_item){
			data["add_item"] = true;
			form = $('#csrf_token_form');
		}
		if(minus_item){
			data["minus_item"] = true;
			form = $('#csrf_token_form');
		}

		var url = form.attr("action");
		console.log(data);

		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			
			success: function(data){
				console.log("ok");
				console.log(data);
				console.log(data.product_total_number);
				if(data.product_total_number||data.product_total_number==0){
					$('#all_price_text h4').text('('+data.product_total_number+')');
					console.log(data.products);
					var total_price_in_order = 0;
					$('.list_busket ul').html("");//clear list_busket
					$.each(data.products, function(k, v){//showing products in busket ajax
                    	$('.list_busket ul').append('<li>'
                    		+'<div class="busket_flex_container">'+
                    			'<div class="busket_product_name">'
                    				+'<a href="/products/category/product_id/'+v.product_id+'">'+v.product_name+'</a>'+
                    			'</div>'+
                    			'<div class="add_item_busket">'+
									'<a href="#" class="add_item_in_busket" id="add_item_in_busket" data-product_id='+v.id+' data-number='+v.number+'>'+'+'+'</a>'+
								'</div>'+
                    			'<div class="busket_items_number">'+
									'<h4>'+v.number+'</h4>'+
								'</div>'+
								'<div class="minus_item_busket">'+
									'<a href="#" class="minus_item_in_busket" id="minus_item_in_busket" data-product_id='+v.id+' data-number='+v.number+'>'+'-'+'</a>'+
								'</div>'+
								'<div class="busket_price_one_items">'+
									'<h4>'+v.product_price+'</h4>'+
								'</div>'+
								'<div class="total_price_one_position">'+
									'<h4>'+v.total_price+'</h4>'+
								'</div>'+
								'<div class="currency">'+
									'<h4>'+'Грн'+'</h4>'+
								'</div>'+
								'<div class="busket_delete_item">'+
									'<a href="#" class="list_delete" data-product_id='+v.id+'>'+'X'+'</a>'+
								'</div>'+
                    		'</div>'+
        				'</li>');
					})
					console.log(data.all_total_price);// to show all total price in busket
					$('#total_order_price_wrapper').text(data.all_total_price);
					$('#total_order_price_checkout').text(data.all_total_price);
				}
				if(data.product_total_number){
		   			$('.empty_busket').addClass('hidden');
		   			$('#in_checkout_button').removeAttr('href');
		   			$('#in_checkout_button').attr('href', '/orders/checkout');
				}
				else{
					location.reload();
				}
			},
			error: function(data){
				console.log("error");
			}
		})
	}
	
	form.on('submit',function(e){           //add event in the form ('submit')
		e.preventDefault();                 //abolish standard behavior
		var number = $('#number').val();     //get number from buy-form on id
		submit_button = $('.button_buy');//get information abaut product ( in button the atribute data-product_id and data-product_name )
		var product_id = submit_button.data("product_id");
		var product_name = submit_button.data("product_name");
		busketUpdating(product_id, number, is_delete=false, add_item=false, minus_item=false);

	})

	$('.header_burger').on('click', function(e){   //showing burger menu
		e.preventDefault();
		$('.menu_main, .header_burger').toggleClass('toggle_burger');
		$('body').toggleClass('lock');
	}); 

	$('.footer_title_1').on('click', function(e){   //showing footer menu list
		e.preventDefault();
		$('.footer_list_1, .triangle_1').toggleClass('active');
	}); 
	$('.footer_title_2').on('click', function(e){   //showing footer menu list
		e.preventDefault();
		$('.footer_list_2, .triangle_2').toggleClass('active');
	});

	$('.registr_text').on('click', function(e){   //showing autorisation window
		e.preventDefault();
		$('.registr_form').slideToggle();
		$('.registr_form').toggleClass('hidden_form');
		$('.menu_main, .burger_container').toggleClass('hidden_form');
	}); 

    $('#view_password').click(function(){ //view password in login form
        var type = $('#password').attr('type') == "text" ? "password" : 'text';
        c = $(this).text() == "Приховати пароль" ? "Показать пароль" : "Приховати пароль";
        $(this).text(c);
        $('#password').prop('type', type);
    });
        $('#view_password1').click(function(){ //view password in registration form
        var type = $('#password1').attr('type') == "text" ? "password" : 'text';
        c = $(this).text() == "Приховати пароль" ? "Показать пароль" : "Приховати пароль";
        $(this).text(c);
        $('#password1').prop('type', type);
    });
        $('#view_password2').click(function(){ //view password in registration form
        var type = $('#password2').attr('type') == "text" ? "password" : 'text';
        c = $(this).text() == "Приховати пароль" ? "Показать пароль" : "Приховати пароль";
        $(this).text(c);
        $('#password2').prop('type', type);
    });

	function showingBusket(){                        //showing busket window
		$('.busket_items').slideToggle();
		$('.busket_items').toggleClass('hidden');
		$('.menu_main, .burger_container').toggleClass('hidden');
	}

	$('.busket_logo').on('click', function(e){
		e.preventDefault();
		showingBusket();
	});

	$('.username').on('click', function(e){ //showing personal office window
		e.preventDefault();
		$('.office').slideToggle();
		$('.office').toggleClass('hidden_office');
		$('.menu_main, .burger_container').toggleClass('hidden_office');
	});

	$(document).on('click', '.list_delete', function(e){//deleting products in the busket
		e.preventDefault();
		product_id = $(this).data("product_id");
		number = 0;
		busketUpdating(product_id, number, is_delete=true, add_item=false, minus_item=false);
		$(this).closest('li').remove();
	})

	//add item the product in basket
	$(document).on('click', '.add_item_in_busket', function(e){
		e.preventDefault();
		add_button = $(this);
		var product_id = add_button.data("product_id");
		var number = add_button.data("number");
		busketUpdating(product_id, number, is_delete=false, add_item=true, minus_item=false);
	})

	//minus item the product in basket
	$(document).on('click', '.minus_item_in_busket', function(e){
		e.preventDefault();
		minus_button = $(this);
		var product_id = minus_button.data("product_id");
		var number = minus_button.data("number");
		busketUpdating(product_id, number, is_delete=false, add_item=false, minus_item=true);
	})

	function calculationBusketAmount(){//підрахунок ціни всіх товарів в корзині та checkout - відображення в html
		var total_order_price =0;
		$('.total-price-one-position-wrapper').each(function(){
			total_order_price += parseFloat($(this).text());
		});
		total_order_price = total_order_price.toFixed(2);
		$('#total_order_price_checkout').text(total_order_price);
		$('#total_order_price_wrapper').text(total_order_price);
	};
	calculationBusketAmount();


	var form_login = $('#form_login');//for autorisation
	form_login.on('submit',function(e){          
		e.preventDefault();  
		console.log("submit");              
		var data = {};
		var csrf_token = $('#form_login [name="csrfmiddlewaretoken"]').val();
		data["csrfmiddlewaretoken"] = csrf_token;
		var username = $('#login').val();
		var password = $('#password').val();
		data["username"] = username;
		data["password"] = password;
		var url = form_login.attr("action");
		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			success: function(data){
				console.log("ok");
				console.log(data);
				if(data.login_success == true){//login windows
					console.log(data.username);
					location.reload();
				}
				else{
					console.log("Такого користувача не існує");	
					$('.error_autorisation').removeClass('hidden_error_aurorisation');
				}

				if(data.need_authorisarion_text == true){
					$('.need_authorisarion_text').addClass('hidden');
				}
				else{
					$('.need_authorisarion_text').removeClass('hidden');
				}

			},
			error: function(data){
				console.log("error");
			}
		})
	})

	$('.link_password_recovery').on('click', function(e){ //for recovery password
		e.preventDefault();
		$('.recovery_password_form ').toggleClass('recovery_password_form_hidden');
	});

	var form_recovery = $('#password_recovery');//for recovery password
	form_recovery.on('submit',function(e){          
		e.preventDefault();  
		console.log("submit");              
		var data = {};
		var csrf_token = $('#password_recovery [name="csrfmiddlewaretoken"]').val();
		data["csrfmiddlewaretoken"] = csrf_token;
		var username = $('#login_recovery_password').val();
		data["username"] = username;
		var url = form_recovery.attr("action");
		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			success: function(data){
				console.log("ok");
				console.log(data);
				if (data.user == true) {
					$('.success_recovery_password').html("");
					$('.error_recovery_password').addClass('error_recovery_password_hidden');
					$('.success_recovery_password').removeClass('success_recovery_password_hidden');
					$('.success_recovery_password').append('<h4>' + 'Новий пароль відправлено на адресу '+ data.email + '</h4>');
				}
				else{
					$('.success_recovery_password').html("");
					$('.success_recovery_password').addClass('success_recovery_password_hidden');
					$('.error_recovery_password').removeClass('error_recovery_password_hidden');
				}
			},
			error: function(data){
				console.log("error");
			}
		})
	})
	//for administration
	$('.add_client_button').on('click', function(e){   //show select user window in part add device
		e.preventDefault();
		$('.select_user_device').toggleClass('display_none_select_user');
		$('.add_new_user').toggleClass('display_none_user');

		var type = $('.add_client_button').attr('type') == "text" ? "button" : 'text';
        c = $(this).text() == "Назад" ? "Додати замовника" : "Назад";
        $(this).text(c);

        required_status = $(".clean").attr("required");
        if (required_status=="required"){
        	$(".clean").attr("required", false);
        }
        else{
        	$(".clean").attr("required", true);
        }

        $(".clean").val(null);//clean field in form
	}); 

	/*for the page creating new device*/
	$(".repair_status_list").change(function(e){
		e.preventDefault();
		/*Коли статус ремонту - "Проведено технічний огляд"*/
		if ($(".repair_status_list").val() == 2) {
        	$('.inspection_device').removeClass("inspection_device_hidden"); 
        	$(".after_inspection").attr("required", true); 
        }
        else{
        	//$(".after_inspection").val(null);
        	$('.inspection_device').addClass("inspection_device_hidden");
        	$(".after_inspection").attr("required", false);
        }

        /*Коли статус ремонту - "Погоджено з замовником"*/
		if ($(".repair_status_list").val() == 3) {
        	$('.agreed_work').removeClass("agreed_work_repair_hidden"); 
        	$(".after_agreed").attr("required", true); 
        }
        else{
        	//$(".after_inspection").val(null);
        	$('.agreed_work').addClass("agreed_work_repair_hidden");
        	$(".after_agreed").attr("required", false);
        }
       	
       	/*Коли статус ремонту - "В очікуванні запчастин"*/
       	if ($(".repair_status_list").val() == 4) {
        	$('.need_spare_part').removeClass("need_spare_hidden");  
        	$(".need_spate_textarea").attr("required", true);
        }
        else{
        	//$(".need_spate_textarea").val(null);
        	$('.need_spare_part').addClass("need_spare_hidden");
        	$(".need_spate_textarea").attr("required", false);
        }

        /*Коли статус ремонту - "Ремонт завершено"*/
        if ($(".repair_status_list").val() == 5) {
        	$('.work_to_device').removeClass("work_device_hidden");
        	$(".work_textarea").attr("required", true);  
        }
        else{
        	//$(".work_textarea").val(null);
        	$('.work_to_device').addClass("work_device_hidden");
        	$(".work_textarea").attr("required", false);
        }

        /*Коли статус ремонту - "Відправлено"*/
        if ($(".repair_status_list").val() == 6) {
        	$('.method_delivery_part').removeClass("delivery_hidden");  
        }
        else{
        	/*$(".invoice_textarea").val(null);
        	$(".delivery_select").val(1);*/
        	$('.method_delivery_part').addClass("delivery_hidden");
        	$('.invoice_part').addClass("invoice_hidden");
        	$(".invoice_textarea").attr("required", false);
        	if ($(".delivery_select").val() == 2) {
        		$('.invoice_part').removeClass("invoice_hidden"); 
       		}
        }
	});

	$(".delivery_select").change(function(e){
		e.preventDefault();
		/*Коли спосіб доставки - "Нова пошта"*/
        if ($(".delivery_select").val() == 2||$(".delivery_select").val() == 5) {
        	$('.invoice_part').removeClass("invoice_hidden");  
        	invoice_required_status = $(".invoice_textarea").attr("required");
        	$(".invoice_textarea").attr("required", true);	
        }
        else{
        	$(".invoice_textarea").val(null);
        	$('.invoice_part').addClass("invoice_hidden");
        	$(".invoice_textarea").attr("required", false);
        }

	});
	/*for the page update information about device*/
	if ($(".repair_status_list").val() == 2) {
        $('.inspection_device').removeClass("inspection_device_hidden");  
    }
    else{
        $('.inspection_device').addClass("inspection_device_hidden");
    }
    if ($(".repair_status_list").val() == 3) {
       	$('.agreed_work').removeClass("agreed_work_repair_hidden"); 
    }
    else{
       	$('.agreed_work').addClass("agreed_work_repair_hidden");
    }

    if ($(".repair_status_list").val() == 4) {
       	$('.need_spare_part').removeClass("need_spare_hidden");  
    }
    else{
       	$('.need_spare_part').addClass("need_spare_hidden");
    }

    if ($(".repair_status_list").val() == 5) {
        $('.work_to_device').removeClass("work_device_hidden");  
    }
    else{
        $('.work_to_device').addClass("work_device_hidden");
    }

    if ($(".repair_status_list").val() == 6) {
        $('.method_delivery_part').removeClass("delivery_hidden");
        if ($(".delivery_select").val() == 2||$(".delivery_select").val() == 5) {
        		$('.invoice_part').removeClass("invoice_hidden"); 
       		} 
    }
    else{
    	$('.delivery_hidden').addClass("delivery_hidden");
    }

	$(".user_search").on("input",function(e){
		e.preventDefault();
		console.log("search");
		search_request=$(e.target).val();

		var form_search_user = $('.search_user_form');
		var data_search = {};
		var csrf_token = $('.search_user_form [name="csrfmiddlewaretoken"]').val();
		data_search["csrfmiddlewaretoken"] = csrf_token;
		data_search["search_request"] = search_request;
		console.log(data_search);
		var url = form_search_user.attr("action");

		$.ajax({
			url: url,
			type: 'POST',
			data: data_search,
			cache: true,
			success: function(data){
				var data_length = data.length;
				$('.select_user').empty();
				$.each(data, function(index, value){
					console.log("Індекс"+index+"; Значення"+value);
				});
				$('.select_user').append('<option value="' + 'False' + '">' + 'Знайдено клієнтів: ' + data_length + '</option>');
				$.each(data, function(key, value) {
					$('.select_user').append('<option value="' + value.id + '">' + value.lastname_client +' '+ value.custumer_phone + '</option>');
				});
				if (data_length==0) {
					$('.valid_inform_repair').removeClass("not_user_hidden");
				}
				else{
					$('.valid_inform_repair').addClass("not_user_hidden");
				}

			},
			error: function(data){
				console.log("error");
			}
		})
	});
	
	$(".type_device_select").change(function(e){
		e.preventDefault();
		var select_type_device=$(".type_device_select").val(); 
		var form_type_device = $('.search_type_device');
		var type_device = {};
		var csrf_token = $('.search_type_device [name="csrfmiddlewaretoken"]').val();
		type_device["csrfmiddlewaretoken"] = csrf_token;
		type_device["search_type_device"] = select_type_device;
		var url = form_type_device.attr("action");
		$.ajax({
			url: url,
			type: 'POST',
			data: type_device,
			cache: true,
			success: function(data){
				$('.select_model_device').empty();
				$.each(data, function(index, value){
					$('.select_model_device').append('<option value="' + value.id + '">' + value.device_model + '</option>');
				});
				if (data.length==0) {
					$('.select_model_device').append('<option value=" " disabled="dicabled" selected>' + 'Моделі цього приладу відсутні' + '</option>');
				}
			},
			error: function(data){
				console.log("error");
			}
		})
	});
	$(".select_model_device").change(function(e){
		e.preventDefault();
		var select_model_device=$(".select_model_device").val(); 
		var form_model_device = $('.search_model_device');
		var model_device = {};
		var csrf_token = $('.search_model_device [name="csrfmiddlewaretoken"]').val();
		model_device["csrfmiddlewaretoken"] = csrf_token;
		model_device["search_model_device"] = select_model_device;
		var url = form_model_device.attr("action");
		$.ajax({
			url: url,
			type: 'POST',
			data: model_device,
			cache: true,
			success: function(data){
				const select = document.querySelector('.type_device_select').getElementsByTagName('option');
				for (let i = 0; i < select.length; i++) {
				    if (select[i].value == data) select[i].selected = true;
				}
			},
			error: function(data){
				console.log("error");
			}
		})
	});
	/*for page def inform_repair, views - device_info*/

	/*робимо кнопку відправки неактивною,якщо клієнта не обрано*/
	if ($(".select_user_devices").val()=="False"){
		$('.button_inform_repair').attr("disabled", true);
		$('.submit_inform_repair').addClass("submit_inform_repair_block");
		$('.inform_repair_datateble').addClass("inform_repair_hidden");
	}
	else{
		$('.button_inform_repair').attr("disabled", false);
		$('.submit_inform_repair').removeClass("submit_inform_repair_block");
		$('.inform_repair_datateble').removeClass("inform_repair_hidden");
	}

	$(".input_from_date, .input_to_date").change(function(e){//змінює дати місцями, якщо дата в полі "З" більше "До"
		e.preventDefault();
		var from_date=$(".input_from_date").val();
		var to_date=$(".input_to_date").val();
		var from_date_object = Date.parse(from_date);
		var to_date_object = Date.parse(to_date);
		if (from_date_object>to_date_object){
			$(".input_from_date").val(to_date);
			$('.input_to_date').val(from_date);
			$('.input_from_date').attr("value", to_date);
			$('.input_to_date').attr("value", from_date);
		}
		else{
			$(".input_from_date").val(from_date);
			$('.input_to_date').val(to_date);
			$('.input_from_date').attr("value", from_date);
			$('.input_to_date').attr("value", to_date);
		}
	});

	function showingInformRepair(){                        //показує історію ремонтів приладів користувача (inform_repair.html)
		var select_user=$(".select_user_devices").val();
		var from_date=$(".input_from_date").val();
		var to_date=$(".input_to_date").val();
		
		var form_choise_user = $('.view_user_devices_form');
		var choise_user = {};
		var csrf_token = $('.view_user_devices_form [name="csrfmiddlewaretoken"]').val();
		choise_user["csrfmiddlewaretoken"] = csrf_token;
		choise_user["calendar_from"] = from_date;
		choise_user["calendar_to"] = to_date;
		if (select_user=="False"){
			$('.inform_repair_datateble').addClass("inform_repair_hidden");
			$('.form_valid_field').removeClass("select_user_input_hidden");
			$('.button_inform_repair').attr("disabled", true);
			$('.submit_inform_repair').addClass("submit_inform_repair_block");
		}
		else{
			$('.inform_repair_datateble').removeClass("inform_repair_hidden");
			$('.form_valid_field').addClass("select_user_input_hidden");
			choise_user["select_user_id"] = select_user;
			var url = form_choise_user.attr("action");
			$.ajax({
				url: url,
				type: 'POST',
				data: choise_user,
				cache: true,
				success: function(data){
					$('.device_in_repair').empty();
					if (data.length==0) {
						$('.inform_repair_datateble').addClass("inform_repair_hidden");
						$('.block_without_device').removeClass("inform_repair_hidden");
						$('.button_inform_repair').attr("disabled", true);
						$('.submit_inform_repair').addClass("submit_inform_repair_block");
					}
					else{
						$('.inform_repair_datateble').removeClass("inform_repair_hidden");
						$('.block_without_device').addClass("inform_repair_hidden");
						$('.button_inform_repair').attr("disabled", false);
						$('.submit_inform_repair').removeClass("submit_inform_repair_block");
					}
					$.each(data, function(index, value){
						$('.device_in_repair').append('<tr align="center">' + "<td>" + '<input type="checkbox" class="checkbox_device" name="selected_device" value="'+ value.id + '">' + "</td>" + 
																"<td>" + "<a href=" + '"' + '../' + 'update_device/' + value.id + '"' + ">" + value.id + "</a>" + "</td>" +
																"<td class='mobile_hidden'>" + "<a href=" + '"' + '../' + 'update_device/' + value.id + '"' + ">" + value.type_devices + "</a>" + "</td>" + 
																"<td>" + value.model_device + "</td>" + 
																"<td class='mobile_hidden'>" + value.repair_status + "</td>" +  
																"<td class='mobile_hidden'>" + value.pay_status + "</td>" +  
																"<td class='mobile_hidden'>" + value.created + "</td>" +  
																"<td class='mobile_hidden_370'>" + value.updated + "</td>" +  
														'</tr>'
														);
					});

					console.log("OK")
				},
				error: function(data){
					console.log("error");
				}
			})
		}
	}

	$(".select_user_devices, .input_from_date, .input_to_date").change(function(e){
		e.preventDefault();
		showingInformRepair();
	});
	$(".select_data").click(function(e){
		e.preventDefault();
		var select_user=$(".select_user_devices").val();
		if (select_user=="False"){
			$('.inform_repair_datateble').addClass("inform_repair_hidden");
			$('.form_valid_field').removeClass("select_user_input_hidden");
			$('.button_inform_repair').attr("disabled", true);
			$('.submit_inform_repair').addClass("submit_inform_repair_block");
		}
		else{
			showingInformRepair();
		}
	});
	$(".user_search_inf_rep").on("input",function(e){
		e.preventDefault();
		$('.inform_repair_datateble').addClass("inform_repair_hidden");
		$('.button_inform_repair').attr("disabled", true);
		$('.submit_inform_repair').addClass("submit_inform_repair_block");
	});
});