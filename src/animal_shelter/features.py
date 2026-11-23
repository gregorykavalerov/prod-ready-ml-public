import numpy as np
import pandas as pd


def add_features(df):
    """Add some features to our data.
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame with data (see load_data)
    Returns
    -------
    with_features : pandas.DataFrame
        DataFrame with some column features added
    """
    df["is_dog"] = _check_is_dog(df["animal_type"])
    # Check if it has a name.
    df["has_name"] = _check_has_name(df["name"])
    # Get sex.
    df["sex"] = _get_sex(df["sex_upon_outcome"])
    # Check if neutered.
    df["neutered"] = _get_neutered(df["sex_upon_outcome"])
    # Get hair type.
    df["hair_type"] = _get_hair_type(df["breed"])
    # Age in days upon outcome.
    df["days_upon_outcome"] = _compute_days_upon_outcome(df["age_upon_outcome"])

    return df


def _check_is_dog(animal_type):
    """Check if the animal is a dog, otherwise return False.
    Parameters
    ----------
    animal_type : pandas.Series
        Type of animal
    Returns
    -------
    result : pandas.Series
        Dog or not
    """
    # Check if it's either a cat or a dog.
    is_cat_dog = animal_type.str.lower().isin(["dog", "cat"])
    if not is_cat_dog.all():
        print("Found something else but dogs and cats:\n%s", animal_type[~is_cat_dog])
        raise RuntimeError("Found pets that are not dogs or cats.")
    is_dog = animal_type.str.lower() == "dog"
    return is_dog


def _check_has_name(name):
    """Check if the animal is not called 'unknown'.
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the animal data including 'name' column.
    Returns
    -------
    has_name : pandas.Series
        Series indicating whether each animal has a name or not.
    """
    has_name = name.str.lower() != "unknown"

    return has_name


def _get_sex(sex_upon_outcome):
    """Determine if the sex was 'Male', 'Female' or unknown.
    Parameters
    ----------
    sex_upon_outcome : pandas.Series
        Series containing the 'sex_upon_outcome' data.
    Returns
    -------
    sex : pandas.Series
        Series indicating the sex of each animal.
    """

    sexUponOutcome = sex_upon_outcome
    sex = pd.Series("unknown", index=sexUponOutcome.index)

    sex.loc[sexUponOutcome.str.endswith("Female")] = "female"
    sex.loc[sexUponOutcome.str.endswith("Male")] = "male"

    return sex


def _get_neutered(sex_upon_outcome):
    """Determine if an animal was intact or not.
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the animal data including 'sex_upon_outcome' column.
    Returns
    -------
    df : pandas.DataFrame
        DataFrame containing the animal data with the 'neutered' column added.
    """

    neutered = sex_upon_outcome
    neutered.loc[neutered.str.contains("Neutered")] = "fixed"
    neutered.loc[neutered.str.contains("Spayed")] = "fixed"

    neutered.loc[neutered.str.contains("Intact")] = "intact"
    neutered.loc[~neutered.isin(["fixed", "intact"])] = "unknown"

    return neutered


def _get_hair_type(breed):
    """Get hair type of a breed.
    Parameters
    ----------
    breed : pandas.Series
        Series containing the 'breed' data.
    Returns
    -------
    hair_type : pandas.Series
        Series containing the hair type of each breed   .
    """

    hair_type = breed.str.lower()
    valid_hair_types = ["shorthair", "medium hair", "longhair"]

    for hair in valid_hair_types:
        is_hair_type = hair_type.str.contains(hair)
        hair_type[is_hair_type] = hair

    hair_type[~hair_type.isin(valid_hair_types)] = "unknown"

    return hair_type


def _compute_days_upon_outcome(age_upon_outcome):
    """Compute age in days upon outcome.
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the animal data including 'age_upon_outcome' column.
    Returns
    -------
    days_upon_outcome : pandas.Series
        Age in days
    """

    Split_Age = age_upon_outcome.str.split()
    time = Split_Age.apply(lambda x: x[0] if x[0] != "Unknown" else np.nan)
    period = Split_Age.apply(lambda x: x[1] if x[0] != "Unknown" else None)
    period_Mapping = {
        "year": 365,
        "years": 365,
        "weeks": 7,
        "week": 7,
        "month": 30,
        "months": 30,
        "days": 1,
        "day": 1,
    }
    days_upon_outcome = time.astype(float) * period.map(period_Mapping)

    return days_upon_outcome
