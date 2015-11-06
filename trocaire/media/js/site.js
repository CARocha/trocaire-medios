$(window).scroll(function() {
    if ($(".menu").offset().top > 50) {
        $(".menu").addClass("fondo");
       
    } else {
        $(".menu").removeClass("fondo");
    }
});
