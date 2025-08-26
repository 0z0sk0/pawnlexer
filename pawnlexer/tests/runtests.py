import pytest
import sys


if __name__ == '__main__':
    return_code = pytest.main(sys.argv[1:])
    sys.exit(return_code)