//// ======== Change Action in Select ==========
//document.getElementById('sidebar_form').model_select.onchange = function() {
//    if (this.value == "all") {
//        var newaction = {% url 'all_catalog' %};
//    } else {
//        var newaction = {% url 'all_catalog' %} + this.value + '/';
//    }
//    document.getElementById('sidebar_form').action = newaction;
//};
//// END action

// ========= FANCYBOX and SLICK =============
// Main/Product image
$('#detail .main-img-slider').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  infinite: false,
  arrows: true,
  fade: true,
  autoplay: false,
  autoplaySpeed: 4000,
  speed: 300,
  lazyLoad: 'ondemand',
  asNavFor: '.thumb-nav',
  prevArrow: '<div class="slick-prev"><i class="i-prev"></i></div>',
  nextArrow: '<div class="slick-next"><i class="i-next"></i></div>'
});

// Thumbnail/alternates
$('.thumb-nav').slick({
  slidesToShow: 2,
  slidesToScroll: 1,
  infinite: false,
  centerPadding: '0px',
  asNavFor: '.main-img-slider',
  dots: false,
  centerMode: false,
  draggable: true,
  speed:200,
  focusOnSelect: true,
  prevArrow: '<div class="slick-prev"><img src="http://127.0.0.1:8000/media/chevron-left-solid.svg"></div>',
  nextArrow: '<div class="slick-next"><i class="i-next"></i><span class="sr-only sr-only-focusable">Next</span></div>',
// SHEMA ROBOCHA
//  responsive: [
//    {
//      breakpoint: 1024,
//      settings: {
//        slidesToShow: 3,
//        slidesToScroll: 3,
//        infinite: true,
//        dots: false
//      }
//    },
//    {
//      breakpoint: 600,
//      settings: {
//        slidesToShow: 2,
//        slidesToScroll: 2
//      }
//    },
//    {
//      breakpoint: 480,
//      settings: {
//        slidesToShow: 1,
//        slidesToScroll: 1
//      }
//    }
//    // You can unslick at a given breakpoint now by adding:
//    // settings: "unslick"
//    // instead of a settings object
//  ]
});

//keeps thumbnails active when changing main image, via mouse/touch drag/swipe
$('.main-img-slider').on('afterChange', function(event, slick, currentSlide, nextSlide){
  //remove all active class
  $('.thumb-nav .slick-slide').removeClass('slick-current');
  //set active class for current slide
  $('.thumb-nav .slick-slide:not(.slick-cloned)').eq(currentSlide).addClass('slick-current');
});
// END Fancybox and Slick


// ============ SIDE Slider Slick =============
$('.side_slide').slick({
  dots: true,
  infinite: true,
  speed: 300,
  slidesToShow: 1,
  adaptiveHeight: true,
  draggable: true,
  autoplay: true,
  autoplaySpeed: 5000,
  prevArrow: '<div class="slick-prev"><i class="i-prev"></i></div>',
  nextArrow: '<div class="slick-next"><i class="i-next"></i></div>',
});
// END side slider


