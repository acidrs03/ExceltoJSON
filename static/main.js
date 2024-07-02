document.getElementById('clearForm').addEventListener('submit', function(event) {
    event.preventDefault();
    fetch('/clear', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        if (data.status) {
            var toastEl = document.getElementById('clearToast');
            var toast = new bootstrap.Toast(toastEl);
            toast.show();
        } else {
            alert('Error clearing files: ' + data.error);
        }
    });
});
