from pydantic import BaseModel, field_validator

class ModelStatistic(BaseModel):
    likes: int 
    viewCount: int 
    contacts: int
    
    @field_validator("likes", "viewCount", "contacts")
    def stats_cannot_be_negative(cls, value): # pylint: disable=no-self-argument
        if value < 0:
            raise ValueError("Statistic value cannot be negative")
        return value
    
    @field_validator("likes", "viewCount", "contacts")
    def stats_not_none_and_not_negative(cls, value):  # pylint: disable=no-self-argument
        if value is None:
            raise ValueError("Statistic value is None")
        if value < 0:
            raise ValueError("Statistic value cannot be negative")
        return value
    
class AdModel(BaseModel):
    id: str            
    sellerId: int      
    name: str          
    price: int         
    statistics: ModelStatistic
    createdAt: str

    @field_validator("id", "sellerId", "name", "price", mode="before")
    def fields_not_none_or_empty(cls, value):  # pylint: disable=no-self-argument
        if value is None:
            raise ValueError("Field is None")
        if isinstance(value, str) and not value.strip():
            raise ValueError("Field is empty")
        return value
    
    @field_validator("sellerId")
    def seller_id_in_range(cls, value): # pylint: disable=no-self-argument
        if not 111111 <= value <= 999999:
            raise ValueError("sellerId must be in range 111111–999999")
        return value
    
    @field_validator("name")
    def name_not_empty(cls, value): # pylint: disable=no-self-argument
        if not value.strip():
            raise ValueError("name is empty")
        return value
    
    @field_validator("price")
    def price_not_negative(cls, value): # pylint: disable=no-self-argument
        if value < 0:
            raise ValueError("price cannot be negative")
        return value
    
    @field_validator("createdAt")
    def created_at_if_present_not_empty(cls, value): # pylint: disable=no-self-argument
        if value is None:
            return value
        if not value.strip():
            raise ValueError("createdAt is empty")
        return value
