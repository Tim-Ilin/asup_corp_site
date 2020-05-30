let form = document.getElementById('accquisition-form');
let selectEmployee = document.getElementById('id_complainant');
let modalPin = document.getElementById('modal-pin-code');
let modalCheckButton = document.getElementById('modal-pin-code__check');
let modalInput = document.getElementById('modal-pin');


let localState = {
    firsTimeModal: true,
};

selectEmployee.addEventListener('change', function () {

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            let responsJson = JSON.parse(xhr.responseText);
            if (localState.firsTimeModal) {
                modalPin.style.display = 'flex';
                form.style.display = 'none';
                modalInput.value = '';
                modalCheckButton.addEventListener('click', function (event) {
                    let getPincode = responsJson[0]['fields']['pin_code'];
                    if (modalInput.value === getPincode.toString()) {
                        modalPin.style.display = 'none';
                        form.style.display = 'block';
                    } else {
                        window.location.href = '/register';
                    }
                })
            }
        }
    }
    xhr.open('GET', `/employee/equipment/${this.value}/`, true);
    xhr.send(null);
});