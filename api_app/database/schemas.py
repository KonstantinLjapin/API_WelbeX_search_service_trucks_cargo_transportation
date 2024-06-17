from pydantic import BaseModel, ValidationError

name_data_tab: list[str] = ["zip", "lat", "lng", "city", "state_id", "state_name", "zcta", "parent_zcta", "population",
                            "density", "county_fips", "county_name", "county_weights", "county_names_all",
                            "county_fips_all", "imprecise", "military", "timezone"]


class Location(BaseModel):
    zip: int
    lat: str
    lng: str
    city: str
    state_id: str
    state_name: str
    zcta: str
    parent_zcta: str
    population: str
    density: str
    county_fips: str
    county_name: str
    county_weights: str
    county_names_all: str
    county_fips_all: str
    imprecise: str
    military: str
    timezone: str
