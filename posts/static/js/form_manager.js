
document.addEventListener("DOMContentLoaded", () => {
    // Selecting couple elements
    const users_posts = document.querySelectorAll(".post-update")
    const modal = document.getElementById("modal")
    const close_button = document.getElementById("close_button")

    // Adding a callback function for each post when the "click" event is triggered
    users_posts.forEach(post => {
        post.addEventListener("click", () => {
            insert_data_on_form(post)
            title_panel_char_count()
            post_content_char_count()
            modal.classList.add("modal-active")
            setTimeout(() => { document.getElementById("title").focus() }, 0500)  // Giving focus to the title field
        })
    })

    // Adding a callback function for the cancel button when the "click" event is triggered
    close_button.addEventListener("click", () => { modal.classList.remove("modal-active") })
})

const insert_data_on_form = post => {
    /*
    This function will get the data that was already fetched from the database and insert it into the form fields. That way, the
    user will remember the stuff it typed there and what needs to be changed/updated.
    */
    // Selecting couple elements
    const title = document.getElementById("title")
    const content = document.getElementById("post_content")
    const post_id = document.getElementById("post_id")

    // Changing their values based on which post the user clicked
    title.value = post.children[0].innerHTML
    content.value = post.children[1].innerHTML
    post_id.value = post.children[3].getAttribute("value")
}
