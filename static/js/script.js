var flag = false;
document.addEventListener("DOMContentLoaded", function () {
  console.log(1);
  var menu = document.getElementById("menu");
  var toggleButton = document.getElementById("menu_but");
  var html =document.getElementById("page")

  toggleButton.addEventListener("mousedown", function () {
    if (flag) {
      menu.style.opacity = "0";
      menu.style.visibility = "hidden";
      html.style.overflow="visible";
      flag = !flag;
    } else {
      menu.style.visibility = "visible";
      menu.style.opacity = "1";
      html.style.overflow="hidden";
      flag = !flag;
    }
  });
});
