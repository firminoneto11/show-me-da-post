const back_to_top_button = document.getElementById('btp')

window.onscroll = () => {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        back_to_top_button.style.display = "block";
    } else {
        back_to_top_button.style.display = "none";
    }
}
