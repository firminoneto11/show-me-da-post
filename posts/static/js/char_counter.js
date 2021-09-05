
const title_panel_char_count = () => {
    // Getting initial data
    const title_input = document.getElementById('title')
    const title_panel = document.getElementById('title_panel')
    // Changing the panel value based in user's input
    title_panel.innerHTML = `${title_input.value.length}/30`
    // Checking if the limited exceeded
    if (title_input.value.length >= 30) {
        title_input.classList.add('error')
    }
    else if ((title_input.className === "input error") && (title_input.value.length < 30)) {
        title_input.classList.remove('error')
    }
}

const post_content_char_count = () => {
    // Getting initial data
    const post_content = document.getElementById('post_content')
    const post_panel = document.getElementById('post_panel')
    // Changing the panel value based in user's input
    post_panel.innerHTML = `${post_content.value.length}/255`
    // Checking if the limited exceeded
    if (post_content.value.length >= 255) {
        post_content.classList.add('error')
    }
    else if ((post_content.className === 'textarea error') && (post_content.value.length < 255)) {
        post_content.classList.remove('error')
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const title = document.getElementById("title")
    const post = document.getElementById('post_content')
    title.addEventListener("input", title_panel_char_count)
    post.addEventListener("input", post_content_char_count)
})
