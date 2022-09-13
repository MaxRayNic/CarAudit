from apps.make_to_model_map.models import MakeToModelsMap
from database import db_session


class AutoCompleteModelQuery:
    @staticmethod
    def get_autocomplete_list(filters, limit):
        make = filters.get('make')
        model_prefix = filters.get('model_prefix')

        filter_query = db_session.query(MakeToModelsMap.model_list, MakeToModelsMap.make).filter(
            MakeToModelsMap.make == make)

        query_result = filter_query.first()
        if query_result is None:
            return []
        model_list = query_result.model_list
        all_model_suggestions = sorted(
            [model for model in model_list if model is not None and model.lower().startswith(model_prefix.lower())],
            key=lambda elem: elem[0].lower())
        return all_model_suggestions[:limit]


class AutoCompleteMakeQuery:
    @staticmethod
    def get_autocomplete_list(filters, limit):
        make_prefix = filters.get('make_prefix', '')

        filter_query = db_session.query(MakeToModelsMap.make).filter(MakeToModelsMap.make.ilike(f'{make_prefix}%')). \
            order_by(MakeToModelsMap.make.asc()).limit(limit)

        query_result = filter_query.all()

        make_suggestions = [each_row.make for each_row in query_result]

        return make_suggestions

