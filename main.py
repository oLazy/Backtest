from bt import utils as btutils
from bt import modelABC
import numpy as np
import pandas as pd
import logging


def main():
    logging.basicConfig(filename="myapp.log", level=logging.INFO)
    logging.info("Start app!")
    btutils.print_version()
    print(pd.__version__)
    calib_input = np.array([1.0, 2.0])
    calib = modelABC.ThisCalibration()
    calib.print_params()
    calib.calibrate(calib_input)
    calib.print_params()
    logging.info("Done!")


if __name__ == '__main__':
    main()
