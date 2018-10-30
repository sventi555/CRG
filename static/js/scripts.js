$('.form-inline').submit((event) => {
    event.preventDefault();
    window.location.replace(`/fields=${$('.form-control').val()}`);
})