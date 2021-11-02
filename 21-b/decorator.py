import logging
import os
from craters import Craters


class ErrorEmptyFile(Exception):
    def __init__(self, name_file, data_file):
        self.file = name_file
        self.data_file = data_file
        logging.error(f"ErrorEmptyFile:{self.file} is EMPTY: {self.data_file}")


class ErrorBrokenMatrix(Exception):
    def __init__(self, name_file, data_file):
        self.file = name_file
        self.data_file = data_file
        logging.error(f"ErrorBrokenMatrix: {self.file} has a broken matrix: {self.data_file}")


class ErrorNotMatrix(Exception):
    def __init__(self, name_file, data_file):
        self.file = name_file
        self.data_file = data_file
        logging.error(f"ErrorNotMatrix: {self.file} has an invalid matrix: {self.data_file}")


class ErrorNotNum(Exception):
    def __init__(self, name_file, data_file):
        self.file = name_file
        self.data_file = data_file
        logging.error(f"ErrorNotNum: {self.file} has a matrix with a character: {self.data_file}")


class Test:

    def check_empty(self, file):
        data_file = craters.read_file(file)
        if len(data_file) == 0:
            raise ErrorEmptyFile(file, data_file)

    def check_rectangle(self, file):
        data_file = craters.read_file(file)
        for i in range(len(data_file)):
            if len(data_file[0]) != len(data_file[i]):
                raise ErrorBrokenMatrix(file, data_file)

    def check_incorrect_num(self, file):
        data_file = craters.read_file(file)
        for i in range(len(data_file)):
            for j in range(len(data_file[0])):
                if data_file[i][j] != '0' and data_file[i][j] != '1':
                    raise ErrorNotNum(file, data_file)

    def check_list(self, file):
        data_file = craters.read_file(file)
        if not isinstance(data_file, list):
            raise ErrorBrokenMatrix(file, data_file)
        for i in range(len(data_file)):
            if not isinstance(data_file[i], list):
                raise ErrorBrokenMatrix(file, data_file)


def benchmark(func):
    def wrapper(*args):
        try:
            logging.info(f"Start working with {args}")
            for item in Test.__dict__:
                to_call = getattr(Test(), item)
                if callable(to_call):
                    to_call(*args)
        except ErrorEmptyFile:
            pass
        except ErrorBrokenMatrix:
            pass
        except ErrorNotMatrix:
            pass
        except ErrorNotNum:
            pass
        else:
            return_value = func(*args)
            # print('craters =', return_value)
            return return_value
        finally:
            logging.info(f"Stop working with {args}")

    return wrapper


@benchmark
def craters_count(files):
    count = craters.check_craters(files)
    return count


logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(message)s')
craters = Craters()
path = "files"
for name_files in os.listdir(path):
    if name_files.endswith(".txt"):
        file_path = f"{path}/{name_files}"
        result = craters_count(file_path)
