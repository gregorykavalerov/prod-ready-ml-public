from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from animal_shelter.data import load_data
from animal_shelter.features import add_features
from animal_shelter.model.config import cat_features, num_features

raw_data = load_data("../data/train.csv")
with_features = add_features(raw_data)

num_transformer = Pipeline(
    steps=[("imputer", SimpleImputer()), ("scaler", StandardScaler())]
)

cat_transformer = Pipeline(steps=[("onehot", OneHotEncoder(drop="first"))])

transformer = ColumnTransformer(
    (
        ("numeric", num_transformer, num_features),
        ("categorical", cat_transformer, cat_features),
    )
)

clf_model = Pipeline(
    [("transformer", transformer), ("model", RandomForestClassifier())]
)

X = with_features[cat_features + num_features]
y = with_features["outcome_type"]

clf_model.fit(X, y)
