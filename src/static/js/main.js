(function($) {
  
  "use strict";  

  $(window).on('load', function() {
	  


/* Add To Cart Tooltip
  ========================================================*/
   $('.btn-cart').tooltip({title: "Add to Cart",});    
   $('.btn-wish').tooltip({title: "Wishlist",});    
   $('.btn-quickview').tooltip({title: "Quick View",});    


  /* slicknav mobile menu active  */
    $('.mobile-menu').slicknav({
        prependTo: '.navbar-header',
        parentTag: 'liner',
        allowParentLinks: true,
        duplicate: true,
        label: '',
        closedSymbol: '<i class="fa fa-angle-right"></i>',
        openedSymbol: '<i class="fa fa-angle-down"></i>',
      });


});  

/* Nav Menu Hover active
========================================================*/
$(".nav > li:has(ul)").addClass("drop");
$(".nav > li.drop > ul").addClass("dropdown");
$(".nav > li.drop > ul.dropdown ul").addClass("sup-dropdown");


/*Page Loader active
========================================================*/
$(window).on('load',function() {
  "use strict";
  $('#loader').fadeOut();
});

/* ==========================================================================
   New Products Owl Carousel
   ========================================================================== */
  $("#new-products").owlCarousel({
      navigation: true,
      pagination: false,
      slideSpeed: 1000,
      stopOnHover: true,
      autoPlay: true,
      items: 4,
      itemsDesktopSmall: [1024, 2],
      itemsTablet: [600, 1],
      itemsMobile: [479, 1]
  });
  $('#new-products').find('.owl-prev').html('<i class="fa fa-angle-left"></i>');
  $('#new-products').find('.owl-next').html('<i class="fa fa-angle-right"></i>');

/* Client Owl Carousel
========================================================*/
$("#client-logo").owlCarousel({
    navigation: false,
    pagination: false,
    slideSpeed: 1000,
    stopOnHover: true,
    autoPlay: true,
    items: 5,
    itemsDesktopSmall: [1024, 3],
    itemsTablet: [600, 1],
    itemsMobile: [479, 1]
});

/* Testimonials Carousel active
========================================================*/
var owl = $(".testimonials-carousel");
  owl.owlCarousel({
    navigation: false,
    pagination: true,
    slideSpeed: 1000,
    stopOnHover: true,
    autoPlay: true,
    items: 1,
    itemsDesktopSmall: [1024, 1],
    itemsTablet: [600, 1],
    itemsMobile: [479, 1]
  });

/* Touch Owl Carousel active
========================================================*/
var owl = $(".touch-slider");
  owl.owlCarousel({
    navigation: true,
    pagination: false,
    slideSpeed: 1000,
    stopOnHover: true,
    autoPlay: true,
    items: 1,
    itemsDesktopSmall: [1024, 1],
    itemsTablet: [600, 1],
    itemsMobile: [479, 1]
  });

$('.touch-slider').find('.owl-prev').html('<i class="fa fa-angle-left"></i>');
$('.touch-slider').find('.owl-next').html('<i class="fa fa-angle-right"></i>');

$('.testimonials-carousel').find('.owl-prev').html('<i class="fa fa-angle-left"></i>');
$('.testimonials-carousel').find('.owl-next').html('<i class="fa fa-angle-right"></i>');

/* owl Carousel active
========================================================*/   
var owl;
$(window).on('load', function() {
    owl = $("#owl-demo");
    owl.owlCarousel({
        navigation: false, // Show next and prev buttons
        slideSpeed: 300,
        paginationSpeed: 400,
        singleItem: true,
        afterInit: afterOWLinit, // do some work after OWL init
        afterUpdate : afterOWLinit
    });

    function afterOWLinit() {
        // adding A to div.owl-page
        $('.owl-controls .owl-page').append('<a class="item-link" />');
        var pafinatorsLink = $('.owl-controls .item-link');
        /**
         * this.owl.userItems - it's your HTML <div class="item"><img src="http://www.ow...t of us"></div>
         */
        $.each(this.owl.userItems, function (i) {
          $(pafinatorsLink[i])
              // i - counter
              // Give some styles and set background image for pagination item
              .css({
                  'background': 'url(' + $(this).find('img').attr('src') + ') center center no-repeat',
                  '-webkit-background-size': 'cover',
                  '-moz-background-size': 'cover',
                  '-o-background-size': 'cover',
                  'background-size': 'cover'
              })
              // set Custom Event for pagination item
              .on('click',function () {
                  owl.trigger('owl.goTo', i);
              });

        });
         // add Custom PREV NEXT controls
        $('.owl-pagination').prepend('<a href="#prev" class="prev-owl"/>');
        $('.owl-pagination').append('<a href="#next" class="next-owl"/>');
        // set Custom event for NEXT custom control
        $(".next-owl").on('click',function () {
            owl.trigger('owl.next');
        });
        // set Custom event for PREV custom control
        $(".prev-owl").on('click',function () {
            owl.trigger('owl.prev');
        });
    }
});

/* Toggle active
========================================================*/
  var o = $('.toggle');
  $(window).on('load', function() {
    $('.toggle').on('click',function (e) {
      e.preventDefault();
      var tmp = $(this);
      o.each(function () {
        if ($(this).hasClass('active') && !$(this).is(tmp)) {
          $(this).parent().find('.toggle_cont').slideToggle();
          $(this).removeClass('active');
        }
      });
      $(this).toggleClass('active');
      $(this).parent().find('.toggle_cont').slideToggle();
    });
    $(window).on('click touchstart', function (e) {
      var container = $(".toggle-wrap");
      if (!container.is(e.target) && container.has(e.target).length === 0 && container.find('.toggle').hasClass('active')) { 
        container.find('.active').toggleClass('active').parent().find('.toggle_cont').slideToggle();
      }
    });
  });
  

/* Back Top Link active
========================================================*/
  var offset = 200;
  var duration = 500;
  $(window).scroll(function() {
    if ($(this).scrollTop() > offset) {
      $('.back-to-top').fadeIn(400);
    } else {
      $('.back-to-top').fadeOut(400);
    }
  });

  $('.back-to-top').on('click',function(event) {
    event.preventDefault();
    $('html, body').animate({
      scrollTop: 0
    }, 600);
    return false;
  })

 /*  Select Color Active
  ========================================================*/
  $("div.color-list .color").click(function(e){
    e.preventDefault();
    $(this).parent().parent().find(".color").removeClass("active");
    $(this).addClass("active");
  })
  

}(jQuery));

 /*  Populate the manufacturer drop down
  ========================================================*/
let dropdown = document.getElementById('drop_manufacturer');
dropdown.length = 0;

let defaultOption = document.createElement('option');
defaultOption.text = 'Select Manufacturer';

dropdown.add(defaultOption);
dropdown.selectedIndex = 10;

const url = 'https://api.myjson.com/bins/c9xcq';

fetch(url)
  .then(
    function(response) {
      if (response.status !== 200) {
        console.warn('Looks like there was a problem. Status Code: ' +
          response.status);
        return;
      }

      // Examine the text in the response
      response.json().then(function(data) {
        let option;
        var uniqueNames = [];
        for (i = 0; i < data.length; i++){
        if(uniqueNames.indexOf(data[i].Manufacturer) === -1){
        uniqueNames.push(data[i].Manufacturer);
        }
        }

    	for (let i = 0; i < uniqueNames.length; i++) {
          option = document.createElement('option');

      	  option.text = uniqueNames[i];
      	 // uniqueNames.sort();   //a proposed way to sort data in alphabetical order
      	 // option.value = data[i].caseID;
      	  dropdown.add(option);

    	}
      });
    }
  )
  .catch(function(err) {
    console.error('Fetch Error -', err);
  });

 /*  Populate model number
  ========================================================*/

let dropdown1 = document.getElementById('drop_model');
dropdown1.length = 0;

let defaultOption1 = document.createElement('option');
defaultOption1.text = 'Select Model';

dropdown1.add(defaultOption1);
dropdown1.selectedIndex = 12;

const url_1 = 'https://api.myjson.com/bins/c9xcq';

fetch(url_1)
  .then(
    function(response) {
      if (response.status !== 200) {
        console.warn('Looks like there was a problem. Status Code: ' +
          response.status);
        return;
      }



      // Examine the text in the response
      response.json().then(function(data) {
        let option1;
        var uniqueNames = [];
        for (i = 0; i < data.length; i++){
        if(uniqueNames.indexOf(data[i].Model) === -1){
        uniqueNames.push(data[i].Model);
        }
        }

    	for (let i = 0; i < uniqueNames.length; i++) {
          option1 = document.createElement('option');

      	  option1.text = uniqueNames[i];
      	 // option.value = data[i].caseID;
      	  dropdown1.add(option1);

    	}
      });
    }
  )
  .catch(function(err) {
    console.error('Fetch Error -', err);
  });



 /*  Populate Manufacturer Year
  ========================================================*/

let dropdown2 = document.getElementById('drop_year');
dropdown2.length = 0;

let defaultOption2 = document.createElement('option');
defaultOption2.text = 'Select Manufactured Year';

dropdown2.add(defaultOption2);
dropdown2.selectedIndex = 10;

const url_2 = 'https://api.myjson.com/bins/c9xcq';

fetch(url_2)
  .then(
    function(response) {
      if (response.status !== 200) {
        console.warn('Looks like there was a problem. Status Code: ' +
          response.status);
        return;
      }



      // Examine the text in the response
      response.json().then(function(data) {
        let option2;
        var uniqueNames = [];
        for (i = 0; i < data.length; i++){
        if(uniqueNames.indexOf(data[i].MakeYear) === -1){
        uniqueNames.push(data[i].MakeYear);
        }
        }

    	for (let i = 0; i < uniqueNames.length; i++) {
          option2 = document.createElement('option');

      	  option2.text = uniqueNames[i];
          uniqueNames.sort();
      	 // option.value = data[i].caseID;
      	  dropdown2.add(option2);

    	}
      });
    }
  )
  .catch(function(err) {
    console.error('Fetch Error -', err);
  });


   /*  Populate Zip code
  ========================================================*/

let dropdown3 = document.getElementById('drop_zip');
dropdown3.length = 0;

let defaultOption3 = document.createElement('option');
defaultOption3.text = 'Select Zip';

dropdown3.add(defaultOption3);
dropdown3.selectedIndex = 18;

const url_3 = 'https://api.myjson.com/bins/c9xcq';

fetch(url_3)
  .then(
    function(response) {
      if (response.status !== 200) {
        console.warn('Looks like there was a problem. Status Code: ' +
          response.status);
        return;
      }



      // Examine the text in the response
      response.json().then(function(data) {
        let option3;
        var uniqueNames = [];
        for (i = 0; i < data.length; i++){
        if(uniqueNames.indexOf(data[i].Zip) === -1){
        uniqueNames.push(data[i].Zip);
        }
        }

    	for (let i = 0; i < uniqueNames.length; i++) {
          option3 = document.createElement('option');

      	  option3.text = uniqueNames[i];
      	 // option.value = data[i].caseID;
      	  dropdown3.add(option3);

    	}
      });
    }
  )
  .catch(function(err) {
    console.error('Fetch Error -', err);
  });



    /*  Populate Category
  ========================================================*/

let dropdown4 = document.getElementById('drop_category');
dropdown4.length = 0;

let defaultOption4 = document.createElement('option');
defaultOption4.text = 'Select Category';

dropdown4.add(defaultOption4);
dropdown4.selectedIndex = 2;

const url_4 = 'https://api.myjson.com/bins/c9xcq';

fetch(url_4)
  .then(
    function(response) {
      if (response.status !== 200) {
        console.warn('Looks like there was a problem. Status Code: ' +
          response.status);
        return;
      }



      // Examine the text in the response
      response.json().then(function(data) {
        let option4;
        var uniqueNames = [];
        for (i = 0; i < data.length; i++){
        if(uniqueNames.indexOf(data[i].Category) === -1){
        uniqueNames.push(data[i].Category);
        }
        }

    	for (let i = 0; i < uniqueNames.length; i++) {
          option4 = document.createElement('option');

      	  option4.text = uniqueNames[i];
      	 // option.value = data[i].caseID;
      	  dropdown4.add(option4);

    	}
      });
    }
  )
  .catch(function(err) {
    console.error('Fetch Error -', err);
  });



//    /*  Populate Price
//  ========================================================*/
//
//let dropdown5 = document.getElementById('drop_price');
//dropdown5.length = 0;
//
//let defaultOption5 = document.createElement('option');
//defaultOption5.text = 'Select Price';
//
//dropdown5.add(defaultOption5);
//dropdown5.selectedIndex = 14;
//
//const url_5 = 'https://api.myjson.com/bins/19mgrv';
//
//fetch(url_5)
//  .then(
//    function(response) {
//      if (response.status !== 200) {
//        console.warn('Looks like there was a problem. Status Code: ' +
//          response.status);
//        return;
//      }
//
//
//
//      // Examine the text in the response
//      response.json().then(function(data) {
//        let option5;
//        var uniqueNames = [];
//        for (i = 0; i < data.length; i++){
//        if(uniqueNames.indexOf(data[i].Price) === -1){
//        uniqueNames.push(data[i].Price);
//        }
//        }
//
//    	for (let i = 0; i < uniqueNames.length; i++) {
//          option5 = document.createElement('option');
//
//      	  option5.text = uniqueNames[i];
//      	 // option.value = data[i].caseID;
//      	  dropdown5.add(option5);
//
//    	}
//      });
//    }
//  )
//  .catch(function(err) {
//    console.error('Fetch Error -', err);
//  });


//
//    /*  Populate Visual Quality
//  ========================================================*/
//
//let dropdown6 = document.getElementById('drop_visual');
//dropdown6.length = 0;
//
//let defaultOption6 = document.createElement('option');
//defaultOption6.text = 'Select Visuals';
//
//dropdown6.add(defaultOption6);
//dropdown6.selectedIndex = 18;
//
//const url_6 = 'https://api.myjson.com/bins/19mgrv';
//
//fetch(url_6)
//  .then(
//    function(response) {
//      if (response.status !== 200) {
//        console.warn('Looks like there was a problem. Status Code: ' +
//          response.status);
//        return;
//      }
//
//
//
//      // Examine the text in the response
//      response.json().then(function(data) {
//        let option6;
//        var uniqueNames = [];
//        for (i = 0; i < data.length; i++){
//        if(uniqueNames.indexOf(data[i].VisualQuality) === -1){
//        uniqueNames.push(data[i].VisualQuality);
//        }
//        }
//
//    	for (let i = 0; i < uniqueNames.length; i++) {
//          option6 = document.createElement('option');
//
//      	  option6.text = uniqueNames[i];
//      	 // option.value = data[i].caseID;
//      	  dropdown6.add(option6);
//
//    	}
//      });
//    }
//  )
//  .catch(function(err) {
//    console.error('Fetch Error -', err);
//  });



    /*  Populate Used Duration
  ========================================================*/

let dropdown7 = document.getElementById('drop_duration');
dropdown7.length = 0;

let defaultOption7 = document.createElement('option');
defaultOption7.text = 'Usage Duration';

dropdown7.add(defaultOption7);
dropdown7.selectedIndex = 17;

const url_7 = 'https://api.myjson.com/bins/c9xcq';

fetch(url_7)
  .then(
    function(response) {
      if (response.status !== 200) {
        console.warn('Looks like there was a problem. Status Code: ' +
          response.status);
        return;
      }



      // Examine the text in the response
      response.json().then(function(data) {
        let option7;
        var uniqueNames = [];
        for (i = 0; i < data.length; i++){
        if(uniqueNames.indexOf(data[i].UsageDuration) === -1){
        uniqueNames.push(data[i].UsageDuration);
        }
        }

    	for (let i = 0; i < uniqueNames.length; i++) {
          option7 = document.createElement('option');

      	  option7.text = uniqueNames[i];
      	 // option.value = data[i].caseID;
      	  dropdown7.add(option7);

    	}
      });
    }
  )
  .catch(function(err) {
    console.error('Fetch Error -', err);
  });



    /*  Populate Country
  ========================================================*/

let dropdown8 = document.getElementById('drop_country');
dropdown8.length = 0;

let defaultOption8 = document.createElement('option');
defaultOption8.text = 'Select Country';

dropdown8.add(defaultOption8);
dropdown8.selectedIndex = 7;

const url_8 = 'https://api.myjson.com/bins/c9xcq';

fetch(url_8)
  .then(
    function(response) {
      if (response.status !== 200) {
        console.warn('Looks like there was a problem. Status Code: ' +
          response.status);
        return;
      }



      // Examine the text in the response
      response.json().then(function(data) {
        let option8;
        var uniqueNames = [];
        for (i = 0; i < data.length; i++){
        if(uniqueNames.indexOf(data[i].Country) === -1){
        uniqueNames.push(data[i].Country);
        }
        }

    	for (let i = 0; i < uniqueNames.length; i++) {
          option8 = document.createElement('option');

      	  option8.text = uniqueNames[i];
      	 // option.value = data[i].caseID;
      	  dropdown8.add(option8);

    	}
      });
    }
  )
  .catch(function(err) {
    console.error('Fetch Error -', err);
  });



    /*  Populate City
  ========================================================*/

let dropdown9 = document.getElementById('drop_city');
dropdown9.length = 0;

let defaultOption9 = document.createElement('option');
defaultOption9.text = 'Select City';

dropdown9.add(defaultOption9);
dropdown9.selectedIndex = 4;
const url_9 = 'https://api.myjson.com/bins/c9xcq';

fetch(url_9)
  .then(
    function(response) {
      if (response.status !== 200) {
        console.warn('Looks like there was a problem. Status Code: ' +
          response.status);
        return;
      }



      // Examine the text in the response
      response.json().then(function(data) {
        let option9;
        var uniqueNames = [];
        for (i = 0; i < data.length; i++){
        if(uniqueNames.indexOf(data[i].City) === -1){
        uniqueNames.push(data[i].City);
        }
        }

    	for (let i = 0; i < uniqueNames.length; i++) {
          option9 = document.createElement('option');

      	  option9.text = uniqueNames[i];
      	 // option.value = data[i].caseID;
      	  dropdown9.add(option9);

    	}
      });
    }
  )
  .catch(function(err) {
    console.error('Fetch Error -', err);
  });




//    /*  Populate Language
//  ========================================================*/
//
//let dropdown11 = document.getElementById('drop_language');
//dropdown11.length = 0;
//
//let defaultOption11 = document.createElement('option');
//defaultOption11.text = 'Select Language';
//
//dropdown11.add(defaultOption11);
//dropdown11.selectedIndex = 8;
//
//const url_11 = 'https://api.myjson.com/bins/19mgrv';
//
//fetch(url_11)
//  .then(
//    function(response) {
//      if (response.status !== 200) {
//        console.warn('Looks like there was a problem. Status Code: ' +
//          response.status);
//        return;
//      }
//
//
//
//      // Examine the text in the response
//      response.json().then(function(data) {
//        let option11;
//        var uniqueNames = [];
//        for (i = 0; i < data.length; i++){
//        if(uniqueNames.indexOf(data[i].Language) === -1){
//        uniqueNames.push(data[i].Language);
//        }
//        }
//
//    	for (let i = 0; i < uniqueNames.length; i++) {
//          option11 = document.createElement('option');
//
//      	  option11.text = uniqueNames[i];
//      	 // option.value = data[i].caseID;
//      	  dropdown11.add(option11);
//
//    	}
//      });
//    }
//  )
//  .catch(function(err) {
//    console.error('Fetch Error -', err);
//  });


//
//    /*  Populate Continent
//  ========================================================*/
//
//let dropdown12 = document.getElementById('drop_continent');
//dropdown12.length = 0;
//
//let defaultOption12 = document.createElement('option');
//defaultOption12.text = 'Select Continent';
//
//dropdown12.add(defaultOption12);
//dropdown12.selectedIndex = 5;
//
//const url_12 = 'https://api.myjson.com/bins/19mgrv';
//
//fetch(url_12)
//  .then(
//    function(response) {
//      if (response.status !== 200) {
//        console.warn('Looks like there was a problem. Status Code: ' +
//          response.status);
//        return;
//      }
//
//
//
//      // Examine the text in the response
//      response.json().then(function(data) {
//        let option12;
//        var uniqueNames = [];
//        for (i = 0; i < data.length; i++){
//        if(uniqueNames.indexOf(data[i].Continent) === -1){
//        uniqueNames.push(data[i].Continent);
//        }
//        }
//
//    	for (let i = 0; i < uniqueNames.length; i++) {
//          option12 = document.createElement('option');
//
//      	  option12.text = uniqueNames[i];
//      	 // option.value = data[i].caseID;
//      	  dropdown12.add(option12);
//
//    	}
//      });
//    }
//  )
//  .catch(function(err) {
//    console.error('Fetch Error -', err);
//  });