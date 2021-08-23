

window.onscroll = () => {
    const back_to_top_button = document.getElementById('btp')
    if (document.body.scrollTop > 30 || document.documentElement.scrollTop > 30) {
        back_to_top_button.style.display = "block";
    } else {
        back_to_top_button.style.display = "none";
    }
}
