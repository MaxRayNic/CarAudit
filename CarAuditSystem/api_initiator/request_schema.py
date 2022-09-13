from flask import Blueprint
from flask_restx import Api, fields

api_v1 = Blueprint("api", __name__, url_prefix="/api/1")
api = Api(api_v1, version="1.0", title="Todo API", description="A simple TODO API", )

ns = api.namespace("", description="TODO operations")

todo = api.model(
    "Todo", {"task": fields.String(required=True, description="The task details")}
)

listed_todo = api.model(
    "ListedTodo",
    {
        "id": fields.String(required=True, description="The todo ID"),
        "todo": fields.Nested(todo, description="The Todo"),
    },
)

average_cost_mileage_filter_parser = api.parser()

average_cost_mileage_filter_parser.add_argument(
    "year", type=str, required=True, help="year of manufacture", location='args'
)
average_cost_mileage_filter_parser.add_argument(
    "make", type=str, required=True, help="brand of the car", location='args'
)
average_cost_mileage_filter_parser.add_argument(
    "model", type=str, required=True, help="model of the car", location='args'
)

car_price_prediction_argument_parser = api.parser()

car_price_prediction_argument_parser.add_argument(
    "year", type=str, required=True, help="year of manufacture", location='args'
)
car_price_prediction_argument_parser.add_argument(
    "make", type=str, required=True, help="make(brand) of the car", location='args'
)
car_price_prediction_argument_parser.add_argument(
    "model", type=str, required=True, help="model of the car", location='args'
)

car_price_prediction_argument_parser.add_argument(
    "desired_mileage", type=float, required=True, help="required mileage for the car", location='args'
)

make_parser = api.parser()

make_parser.add_argument(
    "make_prefix", type=str, required=True, help="make(brand) prefix for make search", location='args'
)
make_parser.add_argument(
    "suggestion_limit", type=int, required=False, default=5, help="maximum no of suggestion for make", location='args'
)

make_model_parser = api.parser()

make_model_parser.add_argument(
    "make", type=str, required=True, help="make of the car", location='args',
)
make_model_parser.add_argument(
    "model_prefix", type=str, required=True, help="model(brand) prefix for autocomplete model search", location='args',
)

make_model_parser.add_argument(
    "suggestion_limit", type=int, required=False, default=5, help="maximum no of suggestion for model", location='args'
)

make_model_year_parser = api.parser()

make_model_year_parser.add_argument(
    "make", type=str, required=True, help="make of the car", location='args',
)
make_model_year_parser.add_argument(
    "model", type=str, required=True, help="model(brand) prefix for autocomplete model search", location='args',
)

make_model_year_parser.add_argument(
    "year_prefix", type=str, required=True, help="year prefix for autocomplete model search", location='args',
)

make_model_year_parser.add_argument(
    "suggestion_limit", type=int, required=False, default=1000, help="maximum no of suggestion for model", location='args'
)

from api_initiator.routes import *