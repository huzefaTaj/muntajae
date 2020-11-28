// slider
var swiper = new Swiper('.swiper-container', {
    slidesPerView: 'auto',
    spaceBetween: 160,
    centerSlides: true,
    grabCursor: true,
    loop: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});

// search
$('.livesearch').on("click", "p", function (e) {
    e.preventDefault();
    $("#location").val($(this).text());
});

function citySearch() {
    // Declare variables
    var input, filter, ul, li, a, i;
    input = document.getElementById('location');
    filter = input.value.toUpperCase();
    ul = document.getElementById("fruits");
    li = ul.getElementsByTagName('li');

    if (input.value.length == 0) {
        ul.style.display = "none";
        return;
    } else {
        ul.style.display = "block";
    }
    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("p")[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "block";
        } else {
            li[i].style.display = "none";
        }
    }
}
function hidee() {
    var ul;
    ul = document.getElementById("fruits");
    ul.style.display = "none";
    // console.log("work");
}

// main search
function filter() {

    var filterValue, input, ul, li, a, i;
    input = document.getElementById("location");
    filterValue = input.value.toUpperCase();
    ul = document.getElementById("Menu");
    li = ul.getElementsByTagName("li");

    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("h4")[0];
        if (a.innerHTML.toUpperCase().indexOf(filterValue) > -1) {
            li[i].style.display = "";

        } else {
            li[i].style.display = "none";
        }
    }
}