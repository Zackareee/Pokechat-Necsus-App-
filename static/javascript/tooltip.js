function reloadAll() 
{
  reloadJs();
  reloadCss();
  
}
// hide menu bar - not useful 
function hideMenu() 
{
  var classvar = document.getElementById("navMenu").classList.remove("is-active");
  var classvar = document.getElementsByClassName("navbar-burger")[0].classList.remove("is-active");           

}

// remove old messages for only one message display
function reloadJs()
{
    var classvar = document.getElementsByClassName("kind-bot")
    for (let i = 1; i < classvar.length; i++) { classvar[i].style.display = "none" }
    var classvar = document.getElementsByClassName("kind-system")
    for (let i = 0; i < classvar.length; i++) { classvar[i].style.display = "none" }
    var classvar = document.getElementsByClassName("kind-user")
    for (let i = 0; i < classvar.length; i++) { classvar[i].style.display = "none" }
}
// change functionality of navbar for better UX
function navbar()
{
  var navbar_onclick = document.getElementsByClassName("navbar-item")
  for (let i = 0; i < navbar_onclick.length; i++) { navbar_onclick[i].onclick = hideMenu }
}

navbar()
reloadJs()



// function reloadStylesheets() {
//   alert('test of js intervals')
// }


// const interval = setInterval(function() {
//   reloadCss()
// }, 60000);

// clearInterval(interval);
// alert('test of js intervals')