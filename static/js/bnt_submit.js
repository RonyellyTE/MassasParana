document.querySelector('form').addEventListener('submit', function (e) {
    const submitBtn = document.querySelector('.submit-btn');
    e.preventDefault();
    submitBtn.classList.add('loading');
    setTimeout(function () {
        submitBtn.classList.remove('loading');
        e.target.submit();  
    }, 3000); 
});     