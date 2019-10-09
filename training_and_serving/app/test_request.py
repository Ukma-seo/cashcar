import requests
import json
import yaml


def preprocess_output(string):
    return string.replace("'", '"').replace("None", "null")


def main():
    cars_params = {
        "body_type": 'Седан',
        "brand_name": 'Toyota',
        "color": "Серый",
        "engine_volume": 2,
        "fuel_type": "Дизель",
        "mileage_value": 30000,
        "model": "Camry",
        "prod_date":2019,
        "transmission":"Автомат",
        "with_auction":0,
        "with_exchange":0
    }

    response1 = requests.get(
        "http://127.0.0.1:5000/app/v1/predict",
        params={"model": "lgbm", "features": json.dumps(cars_params)},
    )
    output1 = response1.text


    for output in [output1,]:
        with open("api_outputs.json", "a", encoding="utf-8") as file:
            data = json.loads(preprocess_output(str(output)))
            json.dump(data, file, ensure_ascii=False, indent=4)
            file.write(",\n")

if __name__ == "__main__":
    main()


cars_params = {"body_type": 'Седан', "brand_name": 'Toyota', "color": "Серый",\
               "engine_volume": 2,"fuel_type": "Дизель",\
               "mileage_value": 30000, "model": "Camry","prod_date":2015,\
               "transmission":"Автомат","with_auction":0,"with_exchange":0}