var flag = false;
document.addEventListener("DOMContentLoaded", function () {
  console.log(1);
  var menu = document.getElementById("menu");
  var toggleButton = document.getElementById("menu_but");
  var upload = document.getElementById("upload");
  var about_us = document.getElementById("about_us");

  toggleButton.addEventListener("mousedown", function () {
    if (flag) {
      menu.style.opacity = "0";
      menu.style.visibility = "hidden";
      flag = !flag;
    } else {
      menu.style.visibility = "visible";
      menu.style.opacity = "1";
      flag = !flag;
    }
    console.log(flag);
  });
});
