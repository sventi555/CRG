$('.form-inline').submit((event) => {
    event.preventDefault();
    console.log("hello");
    window.location.replace(`/fields=${$('.form-control').val()}`);
});

window.onscroll = myFunction;

let navbar = document.getElementById("menu_bar");

let sticky = navbar.offsetTop;

function myFunction() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky");
        $("main").css("padding-top", "3.5em");
    } else {
        navbar.classList.remove("sticky");
        $("main").css("padding-top", "0");
    }
}