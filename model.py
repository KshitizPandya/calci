ERROR_MSG = 'ERROR'

class LengthConverter:
    @staticmethod
    def millimeter_to_centimeter(value):
        try:
            value = float(value)
            result = value / 10
            return str(result)
        except Exception:
            return ERROR_MSG

    @staticmethod
    def centimeter_to_millimeter(value):
        try:
            value = float(value)
            result = value * 10
            return str(result)
        except Exception:
            return ERROR_MSG

    @staticmethod
    def meter_to_centimeter(value):
        try:
            value = float(value)
            result = value * 100
            return str(result)
        except Exception:
            return ERROR_MSG

    @staticmethod
    def centimeter_to_meter(value):
        try:
            value = float(value)
            result = value / 100
            return str(result)
        except Exception:
            return ERROR_MSG

    @staticmethod
    def inch_to_centimeter(value):
        try:
            value = float(value)
            result = value * 2.54
            return str(result)
        except Exception:
            return ERROR_MSG

    @staticmethod
    def centimeter_to_inch(value):
        try:
            value = float(value)
            result = value / 2.54
            return str(result)
        except Exception:
            return ERROR_MSG
