import argparse


def create_parser():
    new_parser = argparse.ArgumentParser()
    new_parser.add_argument('-p', '--productivity', required=True, type=int)
    new_parser.add_argument('-r', '--rate', required=True, type=int)
    new_parser.add_argument('-b', '--bonus', required=True, type=int)
    return new_parser


if __name__ == '__main__':

    parser = create_parser()
    namespace = parser.parse_args()

    print(namespace)

    salary = namespace.productivity * namespace.rate + namespace.bonus

    print(salary)
