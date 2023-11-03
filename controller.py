# Create a Controller class to connect the GUI and the model
from functools import partial
ERROR_MSG = 'ERROR'

from functools import partial
from model import LengthConverter  # Import the LengthConverter class

class Controller:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignals()
    def _calculateResult(self):
        expression = self._view.getDisplayText()
        if "to_cm" in expression:
            parts = expression.split("to_cm")
            if len(parts) == 2:
                value, conversion_type = parts[0], parts[1]
                result = self._evaluate_length_conversion(value, conversion_type)
            else:
                result = ERROR_MSG
        else:
            result = self._evaluate(expression)
        self._view.setDisplayText(result)

    def _evaluate_length_conversion(self, value, conversion_type):
        if conversion_type == 'mm':
            return LengthConverter.millimeter_to_centimeter(value)
        elif conversion_type == 'cm':
            return LengthConverter.centimeter_to_millimeter(value)
        elif conversion_type == 'm':
            return LengthConverter.meter_to_centimeter(value)
        elif conversion_type == 'in':
            return LengthConverter.inch_to_centimeter(value)
        elif conversion_type == 'cm_to_m':
            return LengthConverter.centimeter_to_meter(value)
        elif conversion_type == 'cm_to_in':
            return LengthConverter.centimeter_to_inch(value)
        else:
            return ERROR_MSG

    # Modify the _buildExpression method to include length conversions
    def _buildExpression(self, sub_exp):
        if self._view.getDisplayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.getDisplayText() + sub_exp
        self._view.setDisplayText(expression)