$( document ).ready(function() {
    switch (window.location.pathname){
        case "/lead":
            $(".navbar-nav a:eq(0)").addClass("active");
            break;
        case "/deal":
            $(".navbar-nav a:eq(1)").addClass("active");
            break;
        case "/contact":
            $(".navbar-nav a:eq(2)").addClass("active");
            break;
        case "/company":
            $(".navbar-nav a:eq(3)").addClass("active");
            break;
        default:
            break;
    }
});