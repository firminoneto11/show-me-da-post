
const confirm_deletion = (event) => {
    event.preventDefault()
    swal({
        title: "Are you sure you want to delete this post?",
        text: "Once deleted, no one will be able to see da post!",
        icon: "warning",
        buttons: true,
        dangerMode: true
    }).then((will_delete) => {
        if (will_delete) {
            swal({
                title: "Da post was deleted!",
                text: "Post deleted successfully.",
                icon: "success"
            }).then(_ => event.target.submit())
        }
    })
}

document.addEventListener("DOMContentLoaded", () => {
    const forms = document.getElementById("main").childNodes
    forms.forEach((form) => form.addEventListener("submit", confirm_deletion))
})
