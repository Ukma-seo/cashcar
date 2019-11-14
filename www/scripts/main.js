window.onload = function() {
  init();
};

function init() {
  var data = JSON.parse(`{"transmission": ["Ручная / Механика", "Автомат", "Типтроник", "Адаптивная", "Вариатор"], 
      "color": ["Красный", "Черный", "Белый", "Синий", "Бежевый", "Серый", "Коричневый", "Фиолетовый", "Зеленый", "Желтый", "Оранжевый"]}`);

  Object.keys(data).forEach(value => {
    insertOptions(value, data[value]);
  });
}

function send() {
  var body = {};
  body["prod_date"] = document.getElementById("year").value || "2002";
  body["country"] = document.getElementById("country").value;
  body["body_type"] = document.getElementById("type").value || "Седан";
  body["brand_name"] = document.getElementById("brand").value || "Toyota";
  body["mileage_value"] = document.getElementById("mileage").value || 0;
  body["color"] = document.getElementById("color").value || "Серый";
  body["with_auction"] = 0;
  body["with_exchange"] = 0;
  body["model"] = document.getElementById("model").value || "corolla";
  body["engine_volume"] = document.getElementById("engine_volume").value || 2;
  body["fuel_type"] = document.getElementById("fuel_type").value || "Дизель";
  body["transmission"] =
    document.getElementById("transmission").value || "Автомат";
  for (const key in body) {
    if (!body[key] && body[key] !== 0) {
      delete body[key];
    }
  }
  // var filledParams = Object.keys(body).filter(val => body[val]);
  // var params = filledParams.reduce(
  //   (a, b) => (a += b + "=" + body[b] + "&"),
  //   ""
  // );

  var features = encodeURI(JSON.stringify(body));

  // params = params.slice(0, params.length - 1);
  var url = `http://34.90.123.230:8081/app/v1/predict?model=lgbm&features=${features}`;
  // if (params.length) {
  //   url = url + "?" + params;
  // }

  fetch(url, {
    mode: "no-cors",
    headers: { "Access-Control-Allow-Origin": "*" }
  })
    .then(res =>
      res.hasOwnProperty("json()")
        ? (document.getElementById("response").value = res.json())
        : console.log(res)
    )
    .catch(err => console.log(err));
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
// {"body_type": 'Седан', "brand_name": 'Toyota', "color": "Серый",\
//                "engine_volume": 2,"fuel_type": "Дизель",\
//                "mileage_value": 30000, "model": "Camry","prod_date":2015,\
//                "transmission":"Автомат","with_auction":0,"with_exchange":0}
