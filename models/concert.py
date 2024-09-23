from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.orm import relationship
from utils.tools import Base

class Concert(Base):
    __tablename__ = 'concerts'
    
    id = Column(Integer, primary_key=True)
    band_id = Column(Integer, ForeignKey('bands.id'), nullable=False)
    venue_id = Column(Integer, ForeignKey('venues.id'), nullable=False)
    date = Column(String, nullable=False)
    
    band = relationship("Band", back_populates="concerts")
    venue = relationship("Venue", back_populates="concerts", foreign_keys=[venue_id])

    def fetch_band(self):
        return self.band

    def fetch_venue(self):
        return self.venue
    
    def is_hometown_show(self):
        if self.band and self.venue:
            return self.venue.city.lower() == self.band.hometown.lower()
        return False

    def introduction(self):
        if self.band and self.venue:
            return (f"Hello {self.venue.city}!!!!! We are {self.band.name} from {self.band.hometown}.")
        return "Introduction details are missing."
