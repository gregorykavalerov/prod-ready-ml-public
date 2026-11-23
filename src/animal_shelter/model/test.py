from animal_shelter.data import load_data
from animal_shelter.features import add_features
from animal_shelter.model.config import cat_features, num_features
from animal_shelter.model.train import clf_model

test_data = load_data("../data/test.csv")
with_features = add_features(test_data)

X_test = with_features[cat_features + num_features]

clf_model.predict(X_test)
