$('.mobile-btn').on('click', function (){
    $('.mobile-btn').toggleClass('show-mobile-btn');
    $('.header__nav').toggleClass('show-menu');
    $('.header__nav-menu').toggleClass('show-link');
});


$('.menu a nav').on('click', function (){
    $('.mobile-btn').removeClass('show-mobile-btn');
    $('.header__nav').removeClass('show-menu');
    $('.header__nav-menu').removeClass('show-link');
});
