from enum import Enum
from pydantic import BaseModel, Field
from pathlib import Path
from typing import Union, Optional


class AspectRatio(Enum):
    """Соотношение сторон"""
    FIFTY_BY_FIFTY = "50*50"
    FIFTY_BY_SIXTY = "50*60"
    FIFTY_BY_SEVENTY = "50*70"
    FIFTY_BY_EIGHTY = "50*80"
    FIFTY_BY_NINETY = "50*90"
    FIFTY_BY_ONE_HUNDRED = "50*100"


class Orientation(Enum):
    """Ориентация"""
    HORIZONTAL = "Горизонтальные"
    VERTICAL = "Вертикальные"
    SQUARE = "Квадратные"


class ImageParameters(BaseModel):
    old_name_dir: str = Field(description="Наименование директории, до")
    new_name_dir: str = Field(description="Наименование директории, после")
    new_img_name: str = Field(description="Наименование изображения, после")
    old_full_path_dir: str = Field(description="Полный путь, до")
    new_full_path_dir: str = Field(description="Полный путь, после")
    height: Union[int, float, None] = Field(description="Высота")
    width: Union[int, float, None] = Field(description="Ширина")
    coefficient: Union[int, float, None] = Field(description="Коэффициент")
    aspect_ratio: Optional[str] = Field(description="Соотношение сторон")
    orientation: Optional[str] = Field(description="Ориентация")
    article: int = Field(description="Артикул")
    category: str = Field(description="Категория")
    img_link: str = Field(description="Ссылка на изображение")
    img_name: str = Field(description="Название картины")


class DistributedPictures(ImageParameters):
    new_path: str = Field(description="Полный путь распределения")

