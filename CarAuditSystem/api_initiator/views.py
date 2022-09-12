from flask_restx import Resource

from api_initiator.request_schema import ns, average_cost_mileage_filter_parser, \
    car_price_prediction_argument_parser, make_parser, make_model_parser
from apps.car_details.service import GetAverageMileageAndCostService, PredictPriceByMileageService
from apps.make_to_model_map.service import AutoCompleteMakeService, AutoCompleteModelService


class AverageMileageAndCostView(Resource):
    """Average Calculating View"""

    @ns.doc('get_average')
    @ns.expect(average_cost_mileage_filter_parser)
    def get(self):
        """return average data"""

        arguments = average_cost_mileage_filter_parser.parse_args()
        print(arguments)
        return GetAverageMileageAndCostService(arguments=arguments).execute()


class PredictCarPriceByMileageView(Resource):
    @ns.doc('predict_mileage')
    @ns.expect(car_price_prediction_argument_parser)
    def get(self):
        arguments = car_price_prediction_argument_parser.parse_args()

        return PredictPriceByMileageService(arguments=arguments).execute()


class GetMakeListView(Resource):

    @ns.doc('autocomplete_make')
    @ns.expect(make_parser)
    def get(self):
        arguments = make_parser.parse_args()
        return AutoCompleteMakeService(arguments=arguments).execute()


class GetModeListView(Resource):
    @ns.doc('autocomplete_model')
    @ns.expect(make_model_parser)
    def get(self):
        arguments = make_model_parser.parse_args()
        return AutoCompleteModelService(arguments=arguments).execute()
