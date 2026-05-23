from pydantic import BaseModel


class OpenURLSchema(BaseModel):
    url: str


class GoogleSearchSchema(BaseModel):
    query: str