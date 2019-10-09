import pathlib

DB_HOSTNAME = "localhost"
DB_USERNAME = "simple_user"
DB_NAME = "apartments"
DB_PORT = 5432
TABLE_NAME = "apartments"

DB_PATH = f"postgresql://{DB_USERNAME}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}"

DATA_PATH = "./data/cleaned_data.csv"

# CAT_FEATURES = ["offer_type", "wall_type", "heating", "city_id"]

# COLS_TO_REMOVE = ["title", "absolute_url", "city_name", "price_usd"]

BOOL_FEATURES = []

CAT_FEATURES = ['body_type', 'brand_name', 'color', 'fuel_type', 'model', 'with_auction',
                'with_exchange', 'transmission']

NUM_FEATURES = ['engine_volume',
                'mileage_value',
                'model_years_old']

COLS_TO_REMOVE = ["is_repaired", "is_damaged"]

#
# NUM_FEATURES = [
#     "position",
#     "len_of_description",
#     "floor_located",
#     "number_of_floors_in_the_house",
#     "longitude",
#     "apartment_area",
#     "years_elapsed",
#     "num_of_punctuations_in_description",
#     "number_rooms",
#     "latitude",
#     "num_of_uppercase_letters_in_description",
#     "number_of_images_attached",
# ]

TARGET_COLUMN = "price"

ASSETS_PATH = pathlib.Path("assets")
LGB_PATH = ASSETS_PATH / "lgb_model.jblib"
DT_PATH = ASSETS_PATH / "decision_tree.jblib"
DNN_PATH = ASSETS_PATH / "dnn.pt"
FEATURES_PATH = ASSETS_PATH / "features_train.jblib"
COLUMN_TRANSFORMER_PATH = ASSETS_PATH / "column_transformer.jblib"


REPORT_PATH = "report.md"

SAMPLE_SIZE_FOR_SPEED_INFERENCE = 1000
DNN_TRAIN_TEST_SPLIT_SIZE = 0.2

DNN_DEFAULT_FEATURES_NUM = 2996
DNN_DEFAULT_HIDDEN_UNITS_DIM = 4096
DNN_LR = 1e-2
DNN_NUM_EPOCHS = 100
