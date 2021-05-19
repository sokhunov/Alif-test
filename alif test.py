import operator
import argparse


class FileParser:
    # Actions that can be performed to file values
    ALLOWED_ACTIONS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    def __init__(self, file, action):
        """ Initilize file parser to perform the action """
        self.file = file
        self.action = self.check_action(action)

    def check_action(self, action):
        """
        Check whether action in the class allowed action. Otherwise rise exception
        :param action -> str: user defined action
        :return:
        """
        try:
            return self.ALLOWED_ACTIONS[str(action)]
        except KeyError:
            raise Exception(f"Action '{action}' not found")

    def __call__(self):
        result = self.parse_file()
        print(result)
        return self.save_result(result)

    def parse_file(self):
        """
        Parse the file and perform the action to the values.
        :return -> list: result after the action performed
        """
        with open(self.file) as f:
            result = []
            for line in f:
                a, b = map(int, line.split())
                result.append(self.action(a, b))
        return result

    @staticmethod
    def save_result(values):
        """
        Iterate through values and save the result to the corresponding file: positive in one file negative in another
        :param values:
        :return:
        """
        negative_values_file = r'e:\negative_values.txt'
        positive_values_file = r'e:\positive_values.txt'

        negative_file = open(negative_values_file, 'w')
        positive_file = open(positive_values_file, 'w')

        for val in values:
            if val < 0:
                negative_file.write(str(val) + '\n')
            else:
                positive_file.write(str(val) + '\n')

        negative_file.close()
        positive_file.close()
        return True


parser = argparse.ArgumentParser(description='Perform action for file values')
parser.add_argument('file', type=str, help=r"File full path (e.g c:\\file.txt)")
parser.add_argument('action', type=str, help=r"Action perform to the file values (e.g '+', '-', '/', '*'")
args = parser.parse_args()

FileParser(args.file, args.action)


