$(document).ready(function(){
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