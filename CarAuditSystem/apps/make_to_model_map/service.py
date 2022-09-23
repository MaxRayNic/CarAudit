from apps import BaseService
from apps.make_to_model_map.queries import AutoCompleteModelQuery, AutoCompleteMakeQuery


class AutoCompleteModelService(BaseService):

    def execute(self):
        filters = self.parameters
        suggestion_limit = filters.pop('suggestion_limit', 5)
        return AutoCompleteModelQuery.get_autocomplete_list(filters, suggestion_limit)


class AutoCompleteMakeService(BaseService):

    def execute(self):
        filters = self.parameters
        suggestion_limit = filters.pop('suggestion_limit', 5)
        return AutoCompleteMakeQuery.get_autocomplete_list(filters, suggestion_limit)
