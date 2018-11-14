$('.form-inline').submit((event) => {
    event.preventDefault();
    console.log("hello");
    window.location.replace(`/fields=${$('.form-control').val()}`);
});

window.onscroll = myFunction;

let navbar = document.getElementById("menu_bar");

let sticky = navbar.offsetTop;

window.onresize = () => {
    sticky = navbar.offsetTop;
};

function myFunction() {
    let offset = navbar.offsetHeight;
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky");
        $("main").css("padding-top", `${offset}px`);
    } else {
        navbar.classList.remove("sticky");
        $("main").css("padding-top", "0");
    }
}