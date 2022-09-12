from api_initiator.request_schema import ns
from api_initiator.views import AverageMileageAndCostView, PredictCarPriceByMileageView, GetMakeListView, \
    GetModeListView

ns.add_resource(AverageMileageAndCostView, '/get_average_mileage_and_cost')
ns.add_resource(PredictCarPriceByMileageView, '/car_price_prediction')
ns.add_resource(GetMakeListView, '/make_autocomplete')
ns.add_resource(GetModeListView, '/model_autocomplete')
