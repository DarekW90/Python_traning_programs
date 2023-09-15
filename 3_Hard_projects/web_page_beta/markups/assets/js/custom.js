/**	
	* Template Name: Kevin
	* Version: 1.0	
	* Template Scripts
	* Author: MarkUps
	* Author URI: http://www.markups.io/

	Custom JS
	
	1. FIXED MENU
	2. FEATURED SLIDE ( TYPED SLIDER )
	3. SKILL PROGRESS BAR
	4. MENU SMOOTH SCROLLING
	5. MOBILE MENU CLOSE  
	6. PORTFOLIO GALLERY
	7. PORTFOLIO POPUP VIEW ( IMAGE LIGHTBOX )
	8. CLIENT TUTORIALS ( SLICK SLIDER )
	9. BUTTON SMOOTH SCROLL ( VIEW MY WORK )
	10. RANDOM COLOR THEME
	11. POPUP
	12. LANGAUGE SELECTION
	
**/

(function( $ ){


	/* ----------------------------------------------------------- */
	/*  2. FIXED MENU
	/* ----------------------------------------------------------- */


	jQuery(window).bind('scroll', function () {

    if ($(window).scrollTop() > 100) {

        $('#mu-header').addClass('mu-fixed-nav');
        
	    } else {
	        $('#mu-header').removeClass('mu-fixed-nav');
	    }
	});

		
	/* ----------------------------------------------------------- */
	/*  2. FEATURED SLIDE (TYPED SLIDER)
	/* ----------------------------------------------------------- */

		var typed = new Typed('#typed', {
		    stringsElement: '#typed-strings',
		    typeSpeed: 20,
		    backSpeed: 20,
		    startDelay: 1000,
		    loop: true,
		    loopCount: Infinity
		});

		
	/* ----------------------------------------------------------- */
	/*  3. SKILL PROGRESS BAR
	/* ----------------------------------------------------------- */

		$('.mu-skill-progress-bar').appear(function() {

			$('.mu-python-bar').LineProgressbar({
				percentage: 76,
				triggerOnce: true
			});

			$('.mu-lib-bar').LineProgressbar({
				percentage: 44,
				triggerOnce: true
			});

			$('.mu-msoffice-bar').LineProgressbar({
				percentage: 89,
				triggerOnce: true
			});

			$('.mu-sql-bar').LineProgressbar({
				percentage: 33,
				triggerOnce: true
			});

			$('.mu-other-bar').LineProgressbar({
				percentage: 57,
				triggerOnce: true
			});

			$('.mu-ai-bar').LineProgressbar({
				percentage: 23,
				triggerOnce: true
			});

			$('.mu-html5-bar').LineProgressbar({
				percentage: 57,
				triggerOnce: true
			});

			$('.mu-bootstrap-bar').LineProgressbar({
				percentage: 27,
				triggerOnce: true
			});

		});



	/* ----------------------------------------------------------- */
	/*  4. MENU SMOOTH SCROLLING
	/* ----------------------------------------------------------- */ 

		//MENU SCROLLING WITH ACTIVE ITEM SELECTED

		// Cache selectors
		var lastId,
		topMenu = $(".mu-menu"),
		topMenuHeight = topMenu.outerHeight()+13,
		// All list items
		menuItems = topMenu.find('a[href^=\\#]'),
		// Anchors corresponding to menu items
		scrollItems = menuItems.map(function(){
		  var item = $($(this).attr("href"));
		  if (item.length) { return item; }
		});

		// Bind click handler to menu items
		// so we can get a fancy scroll animation
		menuItems.click(function(e){
		  var href = $(this).attr("href"),
		      offsetTop = href === "#" ? 0 : $(href).offset().top-topMenuHeight+22;
		  jQuery('html, body').stop().animate({ 
		      scrollTop: offsetTop
		  }, 1500);
		  e.preventDefault();
		});

		// Bind to scroll
		jQuery(window).scroll(function(){
		   // Get container scroll position
		   var fromTop = $(this).scrollTop()+topMenuHeight;
		   
		   // Get id of current scroll item
		   var cur = scrollItems.map(function(){
		     if ($(this).offset().top < fromTop)
		       return this;
		   });
		   // Get the id of the current element
		   cur = cur[cur.length-1];
		   var id = cur && cur.length ? cur[0].id : "";
		   
		   if (lastId !== id) {
		       lastId = id;
		       // Set/remove active class
		       menuItems
		         .parent().removeClass("active")
		         .end().filter("[href=\\#"+id+"]").parent().addClass("active");
		   }           
		});


	/* ----------------------------------------------------------- */
	/*  5. MOBILE MENU CLOSE 
	/* ----------------------------------------------------------- */ 

		jQuery('.mu-menu').on('click', 'li a', function() {
		  $('.in').collapse('hide');
		});


	/* ----------------------------------------------------------- */
	/*  6. PORTFOLIO GALLERY
	/* ----------------------------------------------------------- */ 
		$('.filtr-container').filterizr();

		//Simple filter controls

	    $('.mu-simplefilter li').click(function() {
	        $('.mu-simplefilter li').removeClass('active');
	        $(this).addClass('active');
	    });

	/* ----------------------------------------------------------- */
	/*  7. PORTFOLIO POPUP VIEW ( IMAGE LIGHTBOX )
	/* ----------------------------------------------------------- */ 

	$('.mu-filter-imglink').magnificPopup({
	  type: 'image',
	  mainClass: 'mfp-fade',
	  gallery:{
	    enabled:true
	  }
	});

	/* ----------------------------------------------------------- */
	/*  8. CLIENT TUTORIALS (SLICK SLIDER)
	/* ----------------------------------------------------------- */

		$('.mu-tutorial-slide').slick({
		  arrows: false,
		  dots: true,
		  infinite: true,
		  speed: 500,
		  autoplay: true,
		  cssEase: 'linear'
		});


	/* ----------------------------------------------------------- */
	/*  9. BUTTON SMOOTH SCROLL ( VIEW MY WORK )
	/* ----------------------------------------------------------- */

		$('.view-my-work-btn').on('click',function (e) {
		    e.preventDefault();
		    var target = this.hash,
		    $target = $(target);
		    $('html, body').stop().animate({
		        'scrollTop': $target.offset().top
		    }, 1000, 'swing', function () {
		        window.location.hash = target;
			});
		});

	/* ----------------------------------------------------------- */
	/*  10. RANDOM THEME AT THE PAGE REFRESH
	/* ----------------------------------------------------------- */

		$(document).ready(function() {
			// Lista dostępnych motywów
			var motywy = [
				'assets/css/theme-color/bridge-theme.css',
				'assets/css/theme-color/dark-blue-theme.css',
				'assets/css/theme-color/dark-red-theme.css',
				'assets/css/theme-color/default-theme.css',
				'assets/css/theme-color/green-theme.css',
				'assets/css/theme-color/lite-blue-theme.css',
				'assets/css/theme-color/orange-theme.css',
				'assets/css/theme-color/pink-theme.css',
				'assets/css/theme-color/purple-theme.css',
				'assets/css/theme-color/red-theme.css'
			];
		
			// Losowe wybranie motywu
			var losowyMotyw = motywy[Math.floor(Math.random() * motywy.length)];
		
			// Zmiana linku do arkusza stylów
			$('#switcher').attr('href', losowyMotyw);
		});

	/* ----------------------------------------------------------- */
	/*  11. Popup
	/* ----------------------------------------------------------- */

		$(document).ready(function(){
            $('#openBtn').click(function(){
                $('#popup').css('display', 'block');

                var txtContent = $('#txt-content');

                // Tutaj podaj ścieżkę do pliku txt
                var filePath = 'rights/LICENSE.txt';

                $.get(filePath, function(data){
                    txtContent.text(data);
                });
            });

            $('#openBtn2').click(function(){
                $('#popup').css('display', 'block');

                var txtContent = $('#txt-content');

                // Tutaj podaj ścieżkę do pliku txt
                var filePath = 'rights/CREDITS.txt';

                $.get(filePath, function(data){
                    txtContent.text(data);
                });
            });

            $('#closeBtn').click(function(){
                $('#popup').css('display', 'none');
            });
        });

		/* ----------------------------------------------------------- */
		/*  12. Language selection
		/* ----------------------------------------------------------- */
		
		$(document).ready(function() {
            $('#language-select').change(function() {
                var selectedValue = $(this).val();

                var menuHome = $('#menu-home');
                if (selectedValue === 'en') {
                    menuHome.html('HOME')
					;
                } else {
                    menuHome.html('DO GÓRY');
                }

                var menuAbout = $('#menu-about');
                if (selectedValue === 'en') {
                    menuAbout.html('ABOUT ME')
					;
                } else {
                    menuAbout.html('O MNIE');
                }

                var menuProgress = $('#menu-progress');
                if (selectedValue === 'en') {
                    menuProgress.html('PROGRESS')
					;
                } else {
                    menuProgress.html('POSTĘPY');
                }

                var menuTutorials = $('#menu-tutorials');
                if (selectedValue === 'en') {
                    menuTutorials.html('TUTORIALS')
					;
                } else {
                    menuTutorials.html('PORADNIKI');
                }

                var menuContact = $('#menu-contact');
                if (selectedValue === 'en') {
                    menuContact.html('CONTACT')
					;
                } else {
                    menuContact.html('KONTAKT');
                }

                var greeting = $('#start');
                if (selectedValue === 'en') {
                    greeting.html('As a person freshly entering the world of programming and development, I am at the stage of acquiring as much knowledge as possible.<br><br>Every day I learn something new to expand my knowledge.')
					;
                } else {
                    greeting.html('Jako osoba świeżo wkraczająca w świat programowania i rozwoju jestem na etapie zdobywania jak największej wiedzy.<br><br>Każdego dnia uczę się czegoś nowego, poszerzając swoją wiedzę.');
                }
				
                var viewMyWorkBtn = $('#view-my-work-btn');
                if (selectedValue === 'en') {
                    viewMyWorkBtn.html('CHECK MY WORK')
					;
                } else {
                    viewMyWorkBtn.html('ZOBACZ MOJE PRACE');
                }

            });
        });

		
		

	
})( jQuery );



  
	