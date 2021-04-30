import argparse
import add_weight
import processing

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    parser_add_weight = subparsers.add_parser("addweight",
                                              help='add a weight, --date to specify datetime (d/m/yyyy h:m:s)')
    parser_add_weight.add_argument("weight", type=float, help='weight in kg to 1dp')
    parser_add_weight.add_argument("--date", type=str, help='format (d/m/yyyy h:m:s)')

    parser_all = subparsers.add_parser("all")

    parser_days = subparsers.add_parser("days")

    parser_weeks = subparsers.add_parser("weeks")

    args = parser.parse_args()

    if args.command == "addweight":
        add_weight.weight_adder(args.weight, args.date)
    elif args.command == "all":
        processing.plot_all()
    elif args.command == "days":
        processing.plot_days()
    elif args.command == "weeks":
        processing.plot_weeks()
