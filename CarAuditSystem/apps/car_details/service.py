from apps import BaseService
from apps.car_details.queries import  PredictCarPriceByMileageQuery





class PredictPriceByMileageService(BaseService):

    def execute(self):
        filters = self.parameters

        return PredictCarPriceByMileageQuery.predict_price(filters)

