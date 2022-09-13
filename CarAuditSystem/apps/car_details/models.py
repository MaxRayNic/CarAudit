from sqlalchemy import Column, Integer, String, Boolean

from database import Base


class CarDetails(Base):
    __tablename__ = 'car_details'

    id = Column(Integer, primary_key=True)
    vin = Column(String(50))
    year = Column(Integer)
    make = Column(String(273))
    model = Column(String(256))
    trim = Column(String(259))
    dealer_name = Column(String(257))
    dealer_street = Column(String(271))
    dealer_city = Column(String(270))
    dealer_state = Column(String(5))
    dealer_zip = Column(String(60))
    listing_price = Column(Integer)
    listing_mileage = Column(Integer)
    used = Column(Boolean)
    certified = Column(Boolean)
    style = Column(String(255))
    driven_wheels = Column(String(263))
    engine = Column(String(260))
    fuel_type = Column(String(250))
    exterior_color = Column(String(262))
    interior_color = Column(String(261))
    seller_website = Column(String(255))
    first_seen_date = Column(String(100))
    last_seen_date = Column(String(100))
    dealer_vdp_last_seen_date = Column(String(100))
    listing_status = Column(String(100))

    def __init__(self, id, vin, year, make, model, trim, dealer_name, dealer_street, dealer_city, dealer_state,
                 dealer_zip, listing_price, listing_mileage, used, certified, style, driven_wheels, engine, fuel_type,
                 exterior_color, interior_color, seller_website, first_seen_date, last_seen_date,
                 dealer_vdp_last_seen_date, listing_status):
        self.id = id
        self.vin = vin
        self.year = year
        self.make = make
        self.model = model
        self.trim = trim
        self.dealer_name = dealer_name
        self.dealer_street = dealer_street
        self.dealer_city = dealer_city
        self.dealer_state = dealer_state
        self.dealer_zip = dealer_zip
        self.listing_price = listing_price
        self.listing_mileage = listing_mileage
        self.used = used
        self.certified = certified
        self.style = style
        self.driven_wheels = driven_wheels
        self.engine = engine
        self.fuel_type = fuel_type
        self.exterior_color = exterior_color
        self.interior_color = interior_color
        self.seller_website = seller_website
        self.first_seen_date = first_seen_date
        self.last_seen_date = last_seen_date
        self.dealer_vdp_last_seen_date = dealer_vdp_last_seen_date
        self.listing_status = listing_status

    def __repr__(self):
        return '<CarDetails %r>' % (self.id)

    def to_dict(self):
        return {
            "id": self.id,
            "vin": self.vin,
            "year": self.year,
            "make": self.make,
            "model": self.model,
            "trim": self.trim,
            "dealer_name": self.dealer_name,
            "dealer_street": self.dealer_street,
            "dealer_city": self.dealer_city,
            "dealer_state": self.dealer_state,
            "dealer_zip": self.dealer_zip,
            "listing_price": self.listing_price,
            "listing_mileage": self.listing_mileage,
            "used": self.used,
            "certified": self.certified,
            "style": self.style,
            "driven_wheels": self.driven_wheels,
            "engine": self.engine,
            "fuel_type": self.fuel_type,
            "exterior_color": self.exterior_color,
            "interior_color": self.interior_color,
            "seller_website": self.seller_website,
            "first_seen_date": self.first_seen_date,
            "last_seen_date": self.last_seen_date,
            "dealer_vdp_last_seen_date": self.dealer_vdp_last_seen_date,
            "listing_status": self.listing_status
        }
