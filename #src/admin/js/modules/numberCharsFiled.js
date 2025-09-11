/**
 * Подсчет и отображение количества символов в meta-полях
 */

const numberSymbols = {
  'title': 50,
  'description': 140
}

const addLengthChecker = (selector, maxLength) => {
  document.querySelectorAll(selector).forEach((field) => {
    field.addEventListener('input', e => {
      const valueLength = e.currentTarget.value.length;
      const counter = e.currentTarget.previousElementSibling?.querySelector(".meta-length");

      if (counter) {
        counter.innerText = ` ${valueLength}`;
        counter.parentElement.classList.toggle("_red", valueLength > maxLength);
      }
    })
  })
}

addLengthChecker('.meta_title', numberSymbols.title);
addLengthChecker('.meta_description', numberSymbols.description);

