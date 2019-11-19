window.onload = function() {
  init();
};

function init() {
  var data = JSON.parse(
    `{"transmission": ["Ручная / Механика", "Автомат", "Типтроник", "Адаптивная", "Вариатор"],"color": ["Красный", "Черный", "Белый", "Синий", "Бежевый", "Серый", "Коричневый", "Фиолетовый", "Зеленый", "Желтый", "Оранжевый"], "fuel_type": ["Газ/бензин", "Дизель", "Бензин", "Газ", "Электро", "Газ метан", "Гибрид", "Другое", "Газ пропан-бутан"]}`
  );
  // const data = JSON
  Object.keys(data).forEach(value => {
    insertOptions(value, data[value]);
  });
  const options_url = "http://34.90.123.230:8081/app/v1/data";
  fetch(options_url)
    .then(raw => raw.json())
    .then(res =>
      Object.keys(res).forEach(value => {
        insertOptions(value, data[value]);
      })
    )
    .catch(console.error);
}
String.prototype.toUnicode = function() {
  var result = "";
  if (english.test(this)) return this.toString();
  if (isnumber.test(this)) return parseInt(this);
  for (var i = 0; i < this.length; i++) {
    // Assumption: all characters are < 0xffff
    result +=
      "\\" + "u" + ("000" + this[i].charCodeAt(0).toString(16)).substr(-4);
  }
  return result;
};
var english = /^[A-Za-z]*$/;
var isnumber = /^[0-9]*$/;

async function send() {
  var body = {};
  body["prod_date"] =
    document.getElementById("year").value.toUnicode() || "2002".toUnicode();
  body["country"] = document
    .getElementById("country")
    .value.toUnicode()
    .toUnicode();
  body["body_type"] =
    document.getElementById("type").value.toUnicode() || "Седан".toUnicode();
  body["brand_name"] =
    document.getElementById("brand").value.toUnicode() || "Toyota".toUnicode();
  body["mileage_value"] =
    document.getElementById("mileage").value.toUnicode() || 0;
  body["color"] =
    document.getElementById("color").value.toUnicode() || "Серый".toUnicode();
  body["with_auction"] = 0;
  body["with_exchange"] = 0;
  body["model"] =
    document.getElementById("model").value.toUnicode() || "corolla".toUnicode();
  body["engine_volume"] =
    document.getElementById("engine_volume").value.toUnicode() || 2;
  body["fuel_type"] =
    document.getElementById("fuel_type").value.toUnicode() ||
    "Дизель".toUnicode();
  body["transmission"] =
    document.getElementById("transmission").value.toUnicode() ||
    "Автомат".toUnicode();
  for (const key in body) {
    if (!body[key] && body[key] !== 0) {
      delete body[key];
    }
  }

  console.log(body);

  var features = JSON.stringify(body);

  const url = `http://34.90.123.230:8081/app/v1/predict?model=lgbm&features=${features}`;

  const proxyurl = "https://cors-anywhere.herokuapp.com/";
  const raw = await fetch(proxyurl + url);
  const res = await raw.json();
  const price = res["predicted_price"][0];
  document.getElementById("response").innerText = price.toFixed(2) + "$";
}
function insertOptions(selectId, optionsArray) {
  var selectTag = document.getElementById(selectId);
  if (selectTag) {
    var optionTags = makeTags(optionsArray);
    optionTags.forEach(tag => {
      selectTag.innerHTML += tag;
    });
  }
}

function makeTags(optionsArray) {
  return optionsArray.map(
    option => `<option value=${option}>${option}</option>`
  );
}
