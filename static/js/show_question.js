document.addEventListener('DOMContentLoaded', function () {
    fetchData();
    let update = setInterval(() => {
        let div = document.getElementById('time_l');
        let num = parseInt(div.innerText);
        if (num === 1) {
            clearInterval(update);
            submitForm();
        }
        div.innerHTML = num - 1;
    }, 1000);

    document.getElementById('id_form').addEventListener('submit', function (event) {
        event.preventDefault();
        submitForm();
    });

    function submitForm(event) {
        event.preventDefault();
        var form = document.getElementById('id_form');
        fetch("{% url 'question' %}", {
            method: form.method,
            body: new FormData(form)
        })
            .then(function (response) {
                fetchData();
            })
            .catch(function (error) {
                alert(error);
            });
    }
    function fetchData() {
        let host = location.origin;
        var url = host + '{% url "question" %}';
        fetch(url)
            .then(function (response) {
                if (response.redirected === true) {
                    window.location.href = response.url;
                }
                if (!response.ok) {
                    throw new Error("Something went wrong.");
                }
                return response.json();
            })
            .then(function (data) {
                if (data.code === 201) {
                    document.getElementById('d-question').innerHTML = data.question[1];
                    document.getElementById('question-id').value = data.question[0];
                    let holder = document.getElementById('show-option');
                    let txt = "";
                    for (let i of data.options) {
                        txt += `<input type="checkbox" name="option[]" id="option_${i[0]}" value="${i[0]}"> 
                            <label class="checkbox" for="option_${i[0]}">${i[1]}</label><br>`;
                    }
                    holder.innerHTML = txt;
                    let div = document.getElementById('time_l');
                    div.innerHTML = 10;
                } else {
                    throw new Error("Something went wrong.");
                }
            })
            .catch(function (error) {
                alert(error.message);
                window.location.href = location.origin;
            });
    }
});
