document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.tab');
    const forms = document.querySelectorAll('.form');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            forms.forEach(f => f.classList.remove('active'));

            tab.classList.add('active');
            const form = document.getElementById(`${tab.dataset.tab}Form`);
            if (form) form.classList.add('active');
        });
    });

    const validateForm = fields => fields.every(field => field.trim() !== '');

    const sendRequest = async (url, data) => {
        try {
            const res = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            const result = await res.json();
            alert(result.message || 'Операция выполнена успешно!');
            return result;
        } catch (err) {
            console.error(err);
            alert('Ошибка на сервере');
        }
    };

    const handleFormSubmit = async (type, url, fields) => {
        if (!validateForm(fields)) {
            alert('Заполните все поля');
            return;
        }

        const data = type === 'login'
            ? { email: fields[0], password: fields[1] }
            : { email: fields[0], name: fields[1], password: fields[2], password_check: fields[3] };

        const result = await sendRequest(url, data);
        if (result && type === 'login') {
            window.location.href = '/chat';
        }
    };

    // Кнопка входа
    document.getElementById('loginButton').addEventListener('click', e => {
        e.preventDefault();
        const email = document.querySelector('#loginForm input[type="email"]').value;
        const password = document.querySelector('#loginForm input[type="password"]').value;
        handleFormSubmit('login', '/auth/login/', [email, password]);
    });

    document.getElementById('registerButton').addEventListener('click', e => {
        e.preventDefault();
        const email = document.querySelector('#registerForm input[type="email"]').value;
        const name = document.querySelector('#registerForm input[type="text"]').value;
        const password = document.querySelectorAll('#registerForm input[type="password"]')[0].value;
        const password_check = document.querySelectorAll('#registerForm input[type="password"]')[1].value;

        if (password !== password_check) {
            alert('Пароли не совпадают');
            return;
        }

        handleFormSubmit('register', '/auth/register/', [email, name, password, password_check]);
    });
});