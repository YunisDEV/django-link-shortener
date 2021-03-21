const $form = document.querySelector('form.inputs')
const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$form.addEventListener('submit', (e) => {
    e.preventDefault();
    var data = new FormData(e.target)
    document.querySelector('.result').classList.add('hidden')
    $.ajax({
        url: e.target.getAttribute('action'),
        method: "POST",
        data,
        processData: false,
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        contentType: false,
        success: (result) => {
            var $field = document.querySelector('.result > a')
            var ll = $field.getAttribute('data-format').replace('_l_', result.link)
            $field.setAttribute('href', ll)
            $field.innerHTML = ll;
            document.querySelector('.result').classList.remove('hidden')
        }
    })
})


const $input = document.querySelector('[name="original_link"]')
const $modalCloseBtn = document.querySelectorAll('.modal_close')
const $signBtn = document.querySelectorAll('.sign_btn')
const $logoutBtn = document.querySelector('.logout_btn')

if ($input) $input.addEventListener('keyup', e => {
    // console.log(e.target.value)
})

$modalCloseBtn.forEach(i => {
    i.addEventListener('click', e => {
        e.target.parentNode.parentNode.classList.remove('show')
        e.target.parentNode.parentNode.classList.add('hide')
    })
})

if ($signBtn.length > 0) $signBtn.forEach(i => {
    i.addEventListener('click', e => {
        var $el = document.querySelector(`.${i.innerHTML.toLowerCase()}_form`).parentNode.parentNode
        $el.classList.remove('hide')
        $el.classList.add('show')
    })
})

if ($logoutBtn) $logoutBtn.addEventListener('click', e => {
    window.open(e.target.getAttribute('data-to'), '_self')
})