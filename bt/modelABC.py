from abc import ABC, abstractmethod
import datetime as dt
import logging
import numpy as np


class CalibrationABC(ABC):
    def __init__(self):
        self.params = None

    @abstractmethod
    def calibrate(self, data, date=dt.datetime.now()):
        logging.info("{}: Running calibration with data: {}.".format(date.strftime("%d-%m-%Y"), data))


class ThisCalibration(CalibrationABC):

    def calibrate(self, data, date=dt.datetime.now()):
        super().calibrate(data)
        self.params = data
        print("Data: {}".format(data))

    def print_params(self):
        print("This calibration parameters: {}".format(self.params))


class ModelABC(ABC):
    def __init__(self):
        self.params = None
        self.simulation_calendar = None
        self.n_sims = None
        self.result_matrix = np.array([])

    @abstractmethod
    def set_params(self, calibration):
        assert (isinstance(calibration, CalibrationABC))
        self.params = calibration.params

    @abstractmethod
    def simulate(self):
        pass

class ModelGBM(ModelABC):
    def set_params(self, calibration):
        super().set_params()

    def simulate(self, n_sims=1, simulation_calendar=np.array([0])):
        result = np.array()
        for i_sim in range(n_sims):
            for d in simulation_calendar:
                result