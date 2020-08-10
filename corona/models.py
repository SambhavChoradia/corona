from pydantic import BaseModel, Field

class SummaryModel(BaseModel):
    Country: str = Field(...)
    NewConfirmed: int = Field(...)
    TotalConfirmed: int = Field(...)
    NewDeaths: int = Field(...)
    TotalDeaths: int = Field(...)
    NewRecovered: int = Field(...)
    TotalRecovered: int = Field(...)
