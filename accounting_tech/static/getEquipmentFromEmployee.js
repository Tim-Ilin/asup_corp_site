let form = document.getElementById('request-repair');
let selectEmployee = document.getElementById('id_complainant');
let selectOwner = document.getElementById('id_complainant');
let idInventoryNumber = document.getElementById('id_inventory_number');
let modalPin = document.getElementById('modal-pin-code');
let modalCheckButton = document.getElementById('modal-pin-code__check');
let modalInput = document.getElementById('modal-pin');


let localState = {
    firsTime: true,
    firsTimeModal: true,
};

selectEmployee.addEventListener('change', function () {
    if (localState.firsTime) {
        let elLable = document.createElement('label');
        elLable.className = "col-form-label  requiredField";
        elLable.id = "lable_new";
        elLable.innerText = "Выбор техники";
        let elSelect = document.createElement('select');
        elSelect.id = "select-equipment";
        elSelect.className = "select form-control";
        selectOwner.parentNode.insertBefore(elLable, selectOwner.nextSibling);
        elLable.parentNode.insertBefore(elSelect, elLable.nextSibling);
        localState.firsTime = false;
    }

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
            if (responsJson[1]) {
                for (let i = 1; i < responsJson.length; i++) {
                    let selectEquipment = document.getElementById('select-equipment');
                    if (i === 1) {
                        let elOption = document.createElement('option');
                        elOption.id = 'nothing';
                        elOption.innerText = 'Выберите из списка что у вас сломалось';
                        selectEquipment.appendChild(elOption);
                    }
                    let elOption = document.createElement('option');
                    elOption.innerText = responsJson[i]['fields']['name'];
                    elOption.dataset.inventory = responsJson[i]['fields']['inventory_number'];
                    selectEquipment.appendChild(elOption);
                }
            } else {
                let elOption = document.getElementById('lable_new');
                let elOption2 = document.getElementById('select-equipment');
                elOption.style.display = 'none';
                elOption2.style.display = 'none';
            }
        } else {
            let selectEquipment = document.getElementById('select-equipment');
            selectEquipment.innerHTML = '';
        }
    }
    xhr.open('GET', `/employee/equipment/${this.value}/`, true);
    xhr.send(null);
});

form.addEventListener('change', function (event) {
    if (event.target.id === 'select-equipment') {
        let selectEquipment = document.querySelector('#select-equipment');
        idInventoryNumber.value = selectEquipment[selectEquipment.selectedIndex].getAttribute('data-inventory');
    }
});