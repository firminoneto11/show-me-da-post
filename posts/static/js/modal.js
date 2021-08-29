
document.addEventListener("DOMContentLoaded", () => {
    const new_post = document.getElementById("new_post")
    const modal = document.getElementById("modal")
    const close_button = document.getElementById("close_button")
    new_post.addEventListener("click", () => { modal.classList.add("modal-active") })
    close_button.addEventListener("click", () => { modal.classList.remove("modal-active") })
})

// TODO: Find a way to autofocus the id 'title' element when a user clicks on the "New Post" button
