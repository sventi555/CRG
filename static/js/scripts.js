$('.form-inline').submit((event) => {
    event.preventDefault();
    console.log("hello");
    window.location.replace(`/fields=${$('.form-control').val()}`);
})