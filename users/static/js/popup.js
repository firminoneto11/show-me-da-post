
// Function that will manage the behavior of the popup close button
const manage_popup = () => {
    const popup = document.getElementById('popup')
    popup.classList.remove('show')
    popup.classList.add('hide')
}

// Binding the event listeners
document.addEventListener('DOMContentLoaded', () => setTimeout(manage_popup, 5000))
document.getElementById('close_button').addEventListener('click', manage_popup)
