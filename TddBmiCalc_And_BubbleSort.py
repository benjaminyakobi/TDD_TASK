class TddBmiCalc_And_BubbleSort:

    @staticmethod
    def CalcBmi(height, weight):
        return float("{0: .1f}".format(weight / (height * height)))

    @staticmethod
    def CheckIfBmiIsOk(bmi):
        if bmi < 18.5:
            return 'Underweight'
        if bmi >= 18.5:
            if bmi <= 25:
                return 'Healthy'
            if bmi > 25:
                return 'Overweight'