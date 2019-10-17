function send() {
  var body = {};
  body["prod_date"] = document.getElementById("year").value;
  body["country"] = document.getElementById("country").value;
  body["body_type"] = document.getElementById("type").value;
  body["brand_name"] = document.getElementById("brand").value;
  body["mileage_value"] = document.getElementById("mileage").value;
  body["color"] = document.getElementById("color").value;
  body["engine_volume"] = document.getElementById("engine_volume").value;
  body["fuel_type"] = document.getElementById("fuel_type").value;
  body["transmission"] = document.getElementById("transmission").value;
  var filledParams = Object.keys(body).filter(val => body[val]);
  var params = filledParams.reduce(
    (a, b) => (a += b + "=" + body[b] + "&"),
    ""
  );
  params = params.slice(0, params.length - 1);
  var url = "http://localhost:5000/app/v1/predict" + params ? "?" + params : "";
  console.log(body, params, url);
  fetch(url)
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.log(err));
}

// {"body_type": 'Седан', "brand_name": 'Toyota', "color": "Серый",\
//                "engine_volume": 2,"fuel_type": "Дизель",\
//                "mileage_value": 30000, "model": "Camry","prod_date":2015,\
//                "transmission":"Автомат","with_auction":0,"with_exchange":0}
