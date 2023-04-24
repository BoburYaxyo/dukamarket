/***************************************************
==================== JS INDEX ======================
****************************************************
01. PreLoader Js
02. Mobile Menu Js
03. Sidebar Js
04. Cart Toggle Js
05. Search Js
06. Sticky Header Js
07. Data Background Js
08. Testimonial Slider Js
09. Slider Js (Home 3)
10. Brand Js
11. Tesimonial Js
12. Course Slider Js
13. Masonary Js
14. Wow Js
15. Data width Js
16. Cart Quantity Js
17. Show Login Toggle Js
18. Show Coupon Toggle Js
19. Create An Account Toggle Js
20. Shipping Box Toggle Js
21. Counter Js
22. Parallax Js
23. InHover Active Js

****************************************************/

(function ($) {
"use strict";

	var windowOn = $(window);
	////////////////////////////////////////////////////
    // 01. PreLoader Js
	windowOn.on('load',function() {
		$("#loading").fadeOut(500);
	});



	////////////////////////////////////////////////////
    // 06. Sticky Header Js
	windowOn.on('scroll', function () {
		var scroll = $(window).scrollTop();
		if (scroll < 100) {
			$("#header-sticky").removeClass("sticky");
		} else {
			$("#header-sticky").addClass("sticky");
		}
	});


	////////////////////////////////////////////////////
    // 07. Data Background Js
	$("[data-background").each(function () {
		$(this).css("background-image", "url( " + $(this).attr("data-background") + "  )");
	});



	////////////////////////////////////////////////////
    // 13. Masonary Js
	$(".inner__slider").owlCarousel({
		//add owl carousel in activation class
		  loop: true,
		  margin: 40,
		  items: 5,
		  stagePadding: 210,
		  navText: ['<button class="nav-left"><i class="far fa-angle-left"></i></button>', '<button class="nav-right"><i class="far fa-angle-right"></i></button>'],
		  nav: true,
		  dots: false,
		  responsive: {
			0: {
			  items: 1,
			  stagePadding: 10,
			},
			575: {
				items: 1,
				stagePadding: 100,
			},
			767: {
				items: 1,
				stagePadding: 100,
			},
			992: {
				items: 1
			},
			1200: {
				items: 2
			},
			1400: {
			  	items: 3
			},
			
			
			
		  }
	});
	////////////////////////////////////////////////////
    // 14. Wow Js
	new WOW().init();

	
	////////////////////////////////////////////////////
	// 22. Parallax Js
	if ($('.scene').length > 0 ) {
		$('.scene').parallax({
			scalarX: 10.0,
			scalarY: 15.0,
		}); 
	};
})(jQuery);