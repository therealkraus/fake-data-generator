# Standard imports
import random
from typing import Callable

# Related third party imports
import faker
import faker.providers
import pandas as pd

# Local application/library specific imports


def _dirtify(provider_func: Callable, dirty_factor: float = 0.1):
    """Helper function to add some dirty data to the generated data.

    Args:
        provider_func (Callable): A faker function to generate data.
        dirty_factor (float, optional): The probability of generating dirty data. Defaults to 0.1.

    Returns:
        str: The generated data.

    Examples:
        >>> _dirtify(fake.first_name)
        'John'
        >>> _dirtify(fake.first_name, 0.5)
        'N/A'
    """
    dirty_values = [
        None,
        "",
        "N/A",
        "NULL",
        "Invalid",
        "Not Available",
        "Unknown",
        "TBD",
    ]

    if random.random() < dirty_factor:
        return random.choice(dirty_values)
    else:
        return provider_func()


def generate_fake_person_data(localization: str = "en_CA", n: int = 1000):
    """Generate fake person data.

    Args:
        localization (str, optional): The localization of the generated data. Defaults to "en_CA".
        n (int, optional): The number of records to generate. Defaults to 1000.

    Returns:
        dict: A dictionary of generated data.
    """

    fake = faker.Faker(localization, use_weighting=False)

    data = {
        "first_name": [_dirtify(fake.first_name, 0.1) for _ in range(n)],
        "last_name": [_dirtify(fake.last_name, 0.1) for _ in range(n)],
        "street_address": [_dirtify(fake.street_address) for _ in range(n)],
        "city": [_dirtify(fake.city) for _ in range(n)],
        "province": [_dirtify(fake.province_abbr) for _ in range(n)],
        "postal_code": [_dirtify(fake.postalcode) for _ in range(n)],
        "country": [_dirtify(fake.country, 0.15) for _ in range(n)],
        "email": [_dirtify(fake.email) for _ in range(n)],
        "phone_number": [_dirtify(fake.phone_number, 0.3) for _ in range(n)],
        "job": [_dirtify(fake.job, 0.4) for _ in range(n)],
        "ssn": [_dirtify(fake.ssn, 0.5) for _ in range(n)],
        "company": [_dirtify(fake.company) for _ in range(n)],
        "credit_card_number": [
            _dirtify(fake.credit_card_number, 0.0) for _ in range(n)
        ],
        "credit_card_provider": [_dirtify(fake.credit_card_provider) for _ in range(n)],
        "credit_card_expire": [_dirtify(fake.credit_card_expire) for _ in range(n)],
        "credit_card_security_code": [
            _dirtify(fake.credit_card_security_code) for _ in range(n)
        ],
    }

    return data


def generate_fake_company_data(localization: str = "en_CA", n: int = 1000):
    """Generate fake company data.

    Args:
        localization (str, optional): The localization of the generated data. Defaults to "en_CA".
        n (int, optional): The number of records to generate. Defaults to 1000.

    Returns:
        dict: A dictionary of generated data.
    """

    fake = faker.Faker(localization, use_weighting=False)

    data = {
        "company": [_dirtify(fake.company) for _ in range(n)],
        "industry": [_dirtify(fake.company_suffix) for _ in range(n)],
        "catch_phrase": [_dirtify(fake.catch_phrase) for _ in range(n)],
        "bs": [_dirtify(fake.bs) for _ in range(n)],
        "logo": [_dirtify(fake.image_url) for _ in range(n)],
        "street_address": [_dirtify(fake.street_address) for _ in range(n)],
        "city": [_dirtify(fake.city) for _ in range(n)],
        "province": [_dirtify(fake.province_abbr) for _ in range(n)],
        "postal_code": [_dirtify(fake.postalcode) for _ in range(n)],
        "country": [_dirtify(fake.country, 0.15) for _ in range(n)],
        "email": [_dirtify(fake.email) for _ in range(n)],
        "phone_number": [_dirtify(fake.phone_number, 0.3) for _ in range(n)],
        "website": [_dirtify(fake.url) for _ in range(n)],
    }

    return data


def shuffle_data(data: dict) -> pd.DataFrame:
    """Shuffle the rows of a DataFrame.

    Args:
        data (dict): The DataFrame to shuffle.

    Returns:
        pd.DataFrame: The shuffled DataFrame.
    """
    return pd.DataFrame(data).sample(frac=1).reset_index(drop=True)


def save_data(data: pd.DataFrame, filename: str):
    """Save a DataFrame to a CSV file.

    Args:
        data (pd.DataFrame): The DataFrame to save.
        filename (str): The filename to save the DataFrame to.
    """
    data.to_csv(filename, index=False)
