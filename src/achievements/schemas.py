from pydantic import BaseModel


class AchievementsRead(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True