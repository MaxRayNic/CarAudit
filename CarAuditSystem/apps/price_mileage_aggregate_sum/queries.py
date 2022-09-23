from apps.make_to_model_map.models import MakeToModelsMap
from apps.price_mileage_aggregate_sum.models import PriceMileageAggregateSum
from database import db_session


class GetAverageMileageAndCostQuery:

    @staticmethod
    def calc_average_on_make_model_year(filters):
        model = filters.get('model')
        make = filters.get('make')
        year = filters.get('year')

        group_filter_query = db_session.query(PriceMileageAggregateSum). \
            filter(
            PriceMileageAggregateSum.model == model,
            PriceMileageAggregateSum.make == make,
            PriceMileageAggregateSum.year == year
        )

        result = group_filter_query.all()

        result_obj_list = [GetAverageMileageAndCostQuery.object_as_dict(each_row) for each_row in result]
        return result_obj_list

    @staticmethod
    def object_as_dict(obj):
        return {
            'model': obj.model,
            'make': obj.make,
            'year': obj.year,
            'average_price': round(float(obj.total_listing_mileage) / float(obj.car_count), 2),
            'average_mileage': round(float(obj.total_listing_price) / float(obj.car_count), 2)
        }


class AutoCompleteYearQuery:
    @staticmethod
    def get_autocomplete_list(filters, limit):
        model = filters.get('model')
        make = filters.get('make')
        year_prefix = filters.get('year_prefix')

        filter_query = db_session.query(PriceMileageAggregateSum.year).filter(
            PriceMileageAggregateSum.model == model,
            PriceMileageAggregateSum.make == make
        ).\
            order_by(PriceMileageAggregateSum.year.asc()).limit(limit)

        query_result = filter_query.all()

        year_suggestions = [each_row.year for each_row in query_result if str(each_row.year).startswith(year_prefix)]

        return year_suggestions
