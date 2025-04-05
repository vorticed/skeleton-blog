document.addEventListener('DOMContentLoaded', () => {
    function calculateDateDifference() {
        const date1 = new Date(document.getElementById('date1').value);
        const date2 = new Date(document.getElementById('date2').value);
        const diffTime = Math.abs(date2 - date1);
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        document.getElementById('result').innerText = diffDays + ' days';
    }
    // Attach event listener to button
    const button = document.getElementById('calculateButton');
    if (button) {
        button.addEventListener('click', calculateDateDifference);
    }
});


