from apps import BaseService

from apps.price_mileage_aggregate_sum.queries import GetAverageMileageAndCostQuery, AutoCompleteYearQuery


class GetAverageMileageAndCostService(BaseService):

    def execute(self):
        filters = self.parameters
        print(filters)
        return GetAverageMileageAndCostQuery.calc_average_on_make_model_year(filters)


class AutoCompleteYearService(BaseService):

    def execute(self):
        filters = self.parameters
        suggestion_limit = filters.pop('suggestion_limit', 5)
        return AutoCompleteYearQuery.get_autocomplete_list(filters, suggestion_limit)
