
// Function that will manage the behavior of the popup close button
const manage_popup = () => {
    try {
        const popup = document.getElementById('popup')
        popup.classList.remove('show')
        popup.classList.add('hide')
    }
    catch {
        //
    }
}

// Binding the event listeners
document.addEventListener('DOMContentLoaded', () => setTimeout(manage_popup, 2000))
try {
    document.getElementById('close_notification').addEventListener('click', manage_popup)
}
catch {
    //
}
