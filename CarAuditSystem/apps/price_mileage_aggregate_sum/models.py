from sqlalchemy import Column, Integer, String, BigInteger

from database import Base


class PriceMileageAggregateSum(Base):
    __tablename__ = 'price_mileage_aggregate_sum'

    make = Column(String(273), primary_key=True)
    model = Column(String(256))
    year = Column(Integer)
    total_listing_price = Column(BigInteger)
    total_listing_mileage = Column(BigInteger)
    car_count = Column(BigInteger)

    def __init__(self, make, model, year, total_listing_price, total_listing_mileage, car_count):
        self.make = make
        self.model = model
        self.year = year
        self.total_listing_price = total_listing_price
        self.total_listing_mileage = total_listing_mileage
        self.car_count = car_count

    def __repr__(self):
        return '<PriceMileageAggregateSum %r>' % self.make

    def to_dict(self):
        return {

            "make": self.make,
            "model": self.model_list,
            "year": self.year,
            "total_listing_price": self.total_listing_price,
            "total_listing_mileage": self.total_listing_mileage,
            "car_count": self.car_count
        }
