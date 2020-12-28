$(document).ready(function(){
  $("#image_carousel").owlCarousel({
    nav:true,
  	loop:true,
  	dots:false,
  	autoplay:true,
    smartSpeed:1000,
    autoplayTimeout:5000,
    autoplayHoverPause:true,
    responsive:{ //Адаптация в зависимости от разрешения экрана
                0:{
                    items:2
                },
                576:{
                    items:2
                },
                767:{
                    items:3
                },
                992:{
                    items:5
                }
              }

  });
  $("#image_carousel_repair").owlCarousel({
    nav:true,
    loop:true,
    dots:false,
    autoplay:true,
    smartSpeed:1000,
    autoplayTimeout:5000,
    autoplayHoverPause:true,
    responsive:{ //Адаптация в зависимости от разрешения экрана
                0:{
                    items:2
                },
                576:{
                    items:2
                },
                767:{
                    items:3
                },
                992:{
                    items:4
                }
              }

  });
  $('.triangle_link_1').on('click', function(e){   //showing footer menu list
    e.preventDefault();
    $('.list_brand').slideToggle();
    $('.triangle_filter_1, .list_brand').toggleClass('active');
  }); 
  $('.triangle_link_2').on('click', function(e){   //showing footer menu list
    e.preventDefault();
    $('.list_category').slideToggle();
    $('.triangle_filter_2, .list_category').toggleClass('active');
  });

});