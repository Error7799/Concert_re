# Concert Management System

## Overview
This project is a Concert Management System that allows users to manage bands, venues, and concerts. It is built using SQLAlchemy for database interactions and follows a structured approach to model the relationships between different entities.


## Models

### Band
The `Band` class represents a music band with the following attributes:
- `id`: Unique identifier for the band.
- `name`: Name of the band (unique).
- `hometown`: The hometown of the band.
- `date`: The date when the band was formed.

#### Methods:
- `fetch_concerts()`: Returns a list of concerts the band is performing.
- `fetch_venues(session)`: Returns a list of venues where the band has performed.
- `schedule_concert(venue, concert_date)`: Schedules a concert for the band at a given venue and date.
- `all_introductions()`: Returns introductory messages for all concerts.
- `most_performances(session)`: Finds the band with the most performances.

### Venue
The `Venue` class represents a concert venue with the following attributes:
- `id`: Unique identifier for the venue.
- `city`: City where the venue is located.
- `title`: Name of the venue (unique).

#### Methods:
- `get_concerts()`: Returns all concerts held at the venue.
- `get_bands(session)`: Returns all bands that have performed at the venue.
- `concert_on(date, session)`: Returns details of the concert scheduled on a specific date.
- `most_frequent_band(session)`: Finds the band that has performed most frequently at the venue.

### Concert
The `Concert` class represents a concert with the following attributes:
- `id`: Unique identifier for the concert.
- `band_id`: Foreign key referencing the band.
- `venue_id`: Foreign key referencing the venue.
- `date`: Date of the concert.

#### Methods:
- `fetch_band()`: Returns the band performing at the concert.
- `fetch_venue()`: Returns the venue where the concert is held.
- `is_hometown_show()`: Checks if the concert is held in the band's hometown.
- `introduction()`: Returns an introduction message for the concert.

## Usage
To use the Concert Management System:
1. Set up the database using the provided models.
2. Create instances of `Band`, `Venue`, and `Concert` as needed.
3. Use the methods provided to manage and retrieve concert information.

## Dependencies
- SQLAlchemy
- A suitable database (e.g., SQLite, PostgreSQL)

## Run the code
- python app.py

