import requests

from backend.api.endpoints import *
from backend.api.exceptions import (
    APIConnectionError,
    APITimeoutError,
    APIResponseError
)


class OpenF1Client:

    def __init__(self, timeout=30):
        self.base_url = BASE_URL
        self.timeout = timeout

    def get(self, endpoint, params=None):
        try:
            response = requests.get(
                self.base_url + endpoint,
                params=params,
                timeout=self.timeout
            )

            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            raise APITimeoutError()

        except requests.exceptions.ConnectionError:
            raise APIConnectionError()

        except requests.exceptions.HTTPError as e:
            raise APIResponseError(str(e))

    # ---------- Convenience Methods ----------

    def get_meetings(self, **params):
        return self.get(MEETINGS, params)

    def get_sessions(self, **params):
        return self.get(SESSIONS, params)

    def get_drivers(self, **params):
        return self.get(DRIVERS, params)

    def get_weather(self, **params):
        return self.get(WEATHER, params)

    def get_laps(self, **params):
        return self.get(LAPS, params)

    def get_positions(self, **params):
        return self.get(POSITION, params)

    def get_car_data(self, **params):
        return self.get(CAR_DATA, params)

    def get_intervals(self, **params):
        return self.get(INTERVALS, params)

    def get_pit(self, **params):
        return self.get(PIT, params)

    def get_team_radio(self, **params):
        return self.get(TEAM_RADIO, params)

    def get_race_control(self, **params):
        return self.get(RACE_CONTROL, params)

    def get_stints(self, **params):
        return self.get(STINTS, params)

    def get_location(self, **params):
        return self.get(LOCATION, params)
