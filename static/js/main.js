async function cartUpdate(e) {
    const {data} = await axios(e.dataset.url)
    const {message, items_count} = data
    notyf.success({
        message,
        dismissible: true,
        icon: false
    })
    document.getElementById('cart-items-count').innerHTML = items_count
}

async function cartRemove(e) {
    try {
        await axios.get(e.dataset.url); // Corrected axios call syntax
        location.reload(); // Reloading the page after successful removal
    } catch (error) {
        console.error('Error removing item from cart:', error);
    }
}
