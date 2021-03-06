
document.addEventListener("DOMContentLoaded", () => {
    const new_post = document.getElementById("new_post")
    const modal = document.getElementById("modal")
    const close_button = document.getElementById("close_button")
    new_post.addEventListener("click", () => {
        modal.classList.add("modal-active")
        setTimeout(() => { document.getElementById("title").focus() }, 0500)
    })
    close_button.addEventListener("click", () => { modal.classList.remove("modal-active") })
})
