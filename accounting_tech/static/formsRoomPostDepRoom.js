const form = document.querySelector('form');
let el = document.createElement("input");
el.type = 'hidden';
el.name = 'referrer';
el.value = document.referrer;
form.appendChild(el);
