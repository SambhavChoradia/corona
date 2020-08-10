import requests
from prettytable import PrettyTable
from pydantic import BaseModel, Field
from .models import SummaryModel


class Corona:
    def __init__(self):
        self.BASE_URL = "https://api.covid19api.com"

    def get_summary(self):
        """
        get all data and return in formatted table
        """
        response = requests.get(self.BASE_URL + "/summary")

        if response.status_code != 200:
            print("Something went wrong, try again later")
        else:
            table = PrettyTable()
            json_response = response.json()

            table.field_names = [
                "Countries",
                "NewConfirmed",
                "TotalConfirmed",
                "NewDeaths",
                "TotalDeaths",
                "NewRecovered",
                "TotalRecovered",
            ]

            global_data = SummaryModel(**json_response["Global"], Country="Global")
            table.add_row(
                [
                    global_data.Country,
                    global_data.NewConfirmed,
                    global_data.TotalConfirmed,
                    global_data.NewDeaths,
                    global_data.TotalDeaths,
                    global_data.NewRecovered,
                    global_data.TotalRecovered,
                ]
            )

            for value in json_response["Countries"]:
                country_data = SummaryModel(**value)
                table.add_row(
                    [
                        country_data.Country,
                        country_data.NewConfirmed,
                        country_data.TotalConfirmed,
                        country_data.NewDeaths,
                        country_data.TotalDeaths,
                        country_data.NewRecovered,
                        country_data.TotalRecovered,
                    ]
                )
            return table

