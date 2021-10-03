// Basket dropdown hide/show script
$("#menu-icon").click(function (e) {
e.stopPropagation();
$("ul.box").toggle();
});
$("body").click(function () {
$("ul.box").hide();
});

// credit: https://stackoverflow.com/questions/5811122/how-to-trigger-a-click-on-a-link-using-jquery
