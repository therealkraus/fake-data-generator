# Standard imports
import argparse

# Related third party imports

# Local application/library specific imports
from fake_data_generator import services
from fake_data_generator.utils import reset_output_directory, generate_timestamp


def main():
    parser = argparse.ArgumentParser(description="Generate fake data.")
    parser.add_argument(
        "--type",
        type=str,
        default="person",
        help="The type of data to generate. Currently 'person' and 'company' are supported.",
    )
    parser.add_argument(
        "--localization",
        type=str,
        default="en_CA",
        help="The localization of the generated data.",
    )
    parser.add_argument(
        "--n",
        type=int,
        default=1000,
        help="The number of records to generate.",
    )

    args = parser.parse_args()

    if args.type == "person":
        data = services.generate_fake_person_data(args.localization, args.n)
    elif args.type == "company":
        data = services.generate_fake_company_data(args.localization, args.n)
    else:
        print(
            f"Unsupported data type: {args.type}, supported types are 'person' and 'company'."
        )
        return

    reset_output_directory("output")
    timestamp = generate_timestamp()

    data = services.shuffle_data(data)
    services.save_data(data, f"output/{args.type}_{timestamp}.csv")


if __name__ == "__main__":
    main()
