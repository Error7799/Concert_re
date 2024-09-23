from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.orm import relationship
from utils.tools import Base
from sqlalchemy import func

class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    hometown = Column(String, nullable=False)
    date = Column(String, nullable=False)

    concerts = relationship('Concert', back_populates='band')

    def fetch_concerts(self):
        return self.concerts

    def fetch_venues(self, session):
        from models.venue import Venue
        from models.concert import Concert
        return session.query(Venue).join(Concert).filter(Concert.band_id == self.id).all()

    def schedule_concert(self, venue, concert_date):
        from models.concert import Concert
        from utils.tools import SessionLocal
        session = SessionLocal()
        existing_concert = session.query(Concert).filter_by(band_id=self.id, venue_id=venue.id, date=concert_date).first()
        if existing_concert:
            print(f"Concert on {concert_date} at {venue.title} already exists.")
            return existing_concert

        new_concert = Concert(band_id=self.id, venue_id=venue.id, date=concert_date)
        session.add(new_concert)
        session.commit()
        print(f"Successfully scheduled concert for '{self.name}' at '{venue.title}' on {concert_date}.")
        return new_concert

    def all_introductions(self):
        introductions = []
        for concert in self.concerts:
            venue = concert.get_venue()
            intro = f"Hello {venue.city}!!!!! We are {self.name} from {self.hometown}."
            introductions.append(intro)
        return introductions

    @classmethod
    def most_performances(cls, session):
        from models.concert import Concert
        subquery = session.query(
            Concert.band_id,
            func.count(Concert.id).label('performance_count')
        ).group_by(Concert.band_id).subquery()

        most_performances_band_id = session.query(
            subquery.c.band_id
        ).order_by(subquery.c.performance_count.desc()).limit(1).scalar()

        if not most_performances_band_id:
            return "No bands found."

        band = session.query(cls).filter_by(id=most_performances_band_id).first()
        
        if band:
            performance_count = session.query(Concert).filter_by(band_id=band.id).count()
            return (f"Band with most performances:\n"
                    f"Name: {band.name}\n"
                    f"Hometown: {band.hometown}\n"
                    f"Date Formed: {band.date}\n"
                    f"Number of Concerts: {performance_count}")
        else:
            return "Band not found."
