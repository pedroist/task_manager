from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """Base schema with common configurations
    
    This base schema:
    1. Inherits from Pydantic's BaseModel
    2. Sets from_attributes=True which allows converting SQLAlchemy models to Pydantic models
    3. Will be used as the base class for all our other schemas
    """
    model_config = ConfigDict(from_attributes=True)
