
document.addEventListener("DOMContentLoaded", () => {
    const new_post = document.getElementById("new_post")
    const close_button = document.getElementById("close_button")
    const modal = document.getElementById("modal")
    new_post.addEventListener("click", () => { modal.classList.add("modal-active") })
    close_button.addEventListener("click", () => { modal.classList.remove("modal-active") })
})
