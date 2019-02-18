$('.form-inline').submit((event) => {
    event.preventDefault();
    console.log("hello");
    window.location.replace(`/fields=${$('.form-control').val()}`);
});

window.onscroll = myFunction;

let navbar = document.getElementById("menu_bar");

let headerHeight = navbar.offsetTop;

window.onresize = () => {
    headerHeight = $("#site_header").height();
};

function myFunction() {
    let navbarHeight = navbar.offsetHeight;
    if (window.pageYOffset >= headerHeight) {
        navbar.classList.add("sticky");
        $("main").css("padding-top", `${navbarHeight}px`);
    } else {
        navbar.classList.remove("sticky");
        $("main").css("padding-top", "0");
    }
}