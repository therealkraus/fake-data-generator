# Fake Data Generator

This is a simple fake data generator that can be used to generate fake data for testing purposes. You can generate person data and company data. The data is generated using the Faker library.

## Usage

To use the fake data generator, you need to have Python installed on your machine. You can install Python from the [official website](https://www.python.org/).

To generate fake data, you can run the following command:

```bash
python -m fake_data_generator
```

This will generate fake data and save it to a CSV file.

You can specify the number of records to generate by passing the `--n` flag. For example:

```bash
python -m fake_data_generator.py --n 100
```

This will generate 100 records of fake data.

You can also specify the type of data to generate by passing the `--type` flag. For example:

```bash
python -m fake_data_generator --type company
```

This will generate fake company data.

The available types are `person` and `company`.

## License

This project is licensed under the MIT License.
