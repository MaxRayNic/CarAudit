import numpy as np
from sklearn.linear_model import LinearRegression
from sqlalchemy import func

from apps.car_details.models import CarDetails
from database import db_session


# class GetAverageMileageAndCostQuery:
#
#     @staticmethod
#     def calc_average_on_make_model_year(filters):
#         model = filters.get('model')
#         make = filters.get('make')
#         year = filters.get('year')
#
#         group_filter_query = db_session.query(CarDetails.make, CarDetails.model, CarDetails.year,
#                                               func.avg(CarDetails.listing_price).label('average_price'),
#                                               func.avg(CarDetails.listing_mileage).label('average_mileage')). \
#             filter(CarDetails.model == model,
#                    CarDetails.make == make,
#                    CarDetails.year == year,
#                    CarDetails.listing_price.is_not(
#                        None),
#                    CarDetails.listing_mileage.is_not(
#                        None)
#                    ).group_by(CarDetails.model,
#                               CarDetails.make,
#                               CarDetails.year)
#
#         result = group_filter_query.all()
#
#         result_obj_list = [GetAverageMileageAndCostQuery.object_as_dict(each_row) for each_row in result]
#         return result_obj_list
#
#     @staticmethod
#     def object_as_dict(obj):
#         return {
#             'model': obj.model,
#             'make': obj.make,
#             'year': obj.year,
#             'average_price': float(obj.average_price),
#             'average_mileage': float(obj.average_mileage)
#         }


class PredictCarPriceByMileageQuery:

    @staticmethod
    def predict_price(filters):
        model = filters.get('model')
        make = filters.get('make')
        year = filters.get('year')
        desired_mileage = filters.get('desired_mileage')

        group_filter_query = db_session.query(CarDetails.make, CarDetails.model, CarDetails.year,
                                              CarDetails.listing_price,
                                              CarDetails.listing_mileage). \
            filter(CarDetails.model == model,
                   CarDetails.make == make,
                   CarDetails.year == year,
                   CarDetails.listing_price.is_not(
                       None),
                   CarDetails.listing_mileage.is_not(
                       None)
                   )

        result = group_filter_query.all()

        if not result:
            return []
        price_list = [each_row.listing_price for each_row in result]
        mileage_list = [each_row.listing_mileage for each_row in result]

        mileage = np.array(mileage_list).reshape((-1, 1))
        price_list = np.array(price_list)

        regression_model = LinearRegression().fit(mileage, price_list)

        return regression_model.predict([[desired_mileage]]).tolist()


