document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Пример простой проверки
    if (username === 'admin' && password === 'password') {
        window.location.href = 'dashboard.html'; // Перенаправление на главную страницу
    } else {
        document.getElementById('errorMessage').textContent = 'Invalid username or password';
    }
});