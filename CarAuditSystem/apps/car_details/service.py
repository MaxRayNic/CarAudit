from apps import BaseService
from apps.car_details.queries import GetAverageMileageAndCostQuery, PredictCarPriceByMileageQuery


class GetAverageMileageAndCostService(BaseService):

    def execute(self):
        filters = self.parameters
        print(filters)
        return GetAverageMileageAndCostQuery.calc_average_on_make_model_year(filters)


class PredictPriceByMileageService(BaseService):

    def execute(self):
        filters = self.parameters

        return PredictCarPriceByMileageQuery.predict_price(filters)

