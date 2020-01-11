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

    @staticmethod
    def BubbleSort(array):
        if array is None:
            return False
        else:
            size = len(array)
            for i in range(size):
                for j in range(0, size-i-1):
                    if array[j] > array[j+1]:
                        array[j], array[j+1] = array[j+1], array[j]


        return array

    @staticmethod
    def CheckIfEverythingInTheArray(array):
        return all(elem in TddBmiCalc_And_BubbleSort.BubbleSort(array) for elem in array)