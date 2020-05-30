let position = document.getElementById('div_id_post');
let department = document.getElementById('div_id_dept');
let room = document.getElementById('div_id_room');
let positionLink = document.createElement('a');
let departmentLink = document.createElement('a');
let roomLink = document.createElement('a');
let formInput = document.querySelectorAll('input:not([type=hidden]):not([type=submit])');

positionLink.className = 'btn button__edit btn-lg active';
positionLink.role = 'button';
positionLink.href = window.location.origin + '/position/new';
positionLink.textContent = '+';
position.before(positionLink);

departmentLink.className = 'btn button__edit btn-lg active';
departmentLink.role = 'button';
departmentLink.href = window.location.origin + '/departament/new';
departmentLink.textContent = '+';
department.before(departmentLink);

roomLink.className = 'btn button__edit btn-lg active';
roomLink.role = 'button';
roomLink.href = window.location.origin + '/room/new';
roomLink.textContent = '+';
room.before(roomLink);

const setFieldsValueToLocalStorage = () => {
    let objOfValue = {};
    formInput.forEach(function (item, i, arr) {
        objOfValue['urlKey'] = window.location.href;
        objOfValue[item.name] = item.value;
    });
    localStorage.setItem('formValues', JSON.stringify(objOfValue));
};

const fillFieldsFromLocalstorage = () => {
    let objOfValue = JSON.parse(localStorage.getItem('formValues'));
    if (objOfValue) {
        if (objOfValue['urlKey'] === window.location.href) {
            for (let prop in objOfValue) {
                formInput.forEach(function (item, i) {
                    if (prop === item.name) {
                        item.value = objOfValue[prop];
                    }
                })
            }
            localStorage.removeItem('formValues');
        }
    }
};
positionLink.addEventListener('click', setFieldsValueToLocalStorage);
departmentLink.addEventListener('click', setFieldsValueToLocalStorage);
roomLink.addEventListener('click', setFieldsValueToLocalStorage);

document.addEventListener("DOMContentLoaded", () => {
    fillFieldsFromLocalstorage();
})