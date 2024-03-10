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


class FinalTable(BaseModel):
    id: str = Field(description="ID")
    type: str = Field(description="Тип", default="variable")
    article: int = Field(description="Артикул")
    name: str = Field(description="Имя")
    published: int = Field(description="Опубликован", default=1)
    recommended: int = Field(description="рекомендуемый?", default=0)
    visibility_in_the_catalog: str = Field(description="Видимость в каталоге", default="visible")
    short_description: str = Field(description="Краткое описание", default="")
    description: str = Field(description="Описание", default="")
    discount_start_date: str = Field(description="Дата начала действия скидки", default="")
    discount_expiration_date: str = Field(description="Дата окончания действия скидки", default="")
    tax_status: str = Field(description="Статус налога", default="taxable")
    tax_class: str = Field(description="Налоговый класс", default="")
    availability: int = Field(description="В наличии?", default=1)
    stocks: int = Field(description="Запасы", default=1000)
    size_of_small_stocks: str = Field(description="Величина малых запасов", default="")
    pre_order: int = Field(description="Возможен ли предзаказ?", default=0)
    sold_individually: int = Field(description="Продано индивидуально?", default=0)
    weight: str = Field(description="Вес (kg)", default="")
    length: str = Field(description="Длина (cm)", default="")
    width: str = Field(description="Ширина (cm)", default="")
    height: str = Field(description="Высота (cm)", default="")
    feedback: int = Field(description="Разрешить отзывы от клиентов?", default=1)
    purchase_note: str = Field(description="Примечание к покупке", default="")
    promotional_price: str = Field(description="Акционная цена", default="")
    base_price: str = Field(description="Базовая цена", default="")
    category: str = Field(description="Категории")
    tags: str = Field(description="Метки", default="")
    delivery_class: str = Field(description="Класс доставки", default="")
    images: str = Field(description="Изображения")
    download_limit: str = Field(description="Лимит загрузок", default="")
    days_upload_period: str = Field(description="Дней срока загрузки", default="")
    parent: str = Field(description="Родительский", default="")
    grouped_products: str = Field(description="Сгруппированные товары", default="")
    upsale: str = Field(description="Апсейл", default="")
    crossels: str = Field(description="Кросселы", default="")
    external_url: str = Field(description="Внешний URL", default="")
    button_text: str = Field(description="Текст кнопки", default="")
    position: str = Field(description="Позиция", default="")
    attribute_name_1: str = Field(description="Название атрибута 1", default="Размеры")
    attribute_values_1: str = Field(description="Значения атрибутов 1")
    visibility_attribute_1: int = Field(description="Видимость атрибута 1", default=1)
    global_attribute_1: int = Field(description="Глобальный атрибут 1", default=1)
    default_attribute_1: str = Field(description="Атрибут 1 по умолчанию")
    attribute_name_2: str = Field(description="Название атрибута 2", default="Крепления")
    attribute_values_2: str = Field(
        description="Значения атрибутов 2", default="Классические крепления, Липучки на стену"
    )
    visibility_attribute_2: int = Field(description="Видимость атрибута 2", default=1)
    global_attribute_2: int = Field(description="Глобальный атрибут 2", default=1)
    default_attribute_2: str = Field(description="Атрибут 2 по умолчанию", default="Классические крепления")
    attribute_name_3: str = Field(description="Название атрибута 3", default="Материал")
    attribute_values_3: str = Field(description="Значения атрибутов 3", default="Виниловый холст, Хлопковый холст")
    visibility_attribute_3: int = Field(description="Видимость атрибута 3", default=1)
    global_attribute_3: int = Field(description="Глобальный атрибут 3", default=1)
    default_attribute_3: str = Field(description="Атрибут 3 по умолчанию", default="Виниловый холст")
    attribute_name_4: str = Field(description="Название атрибута 4", default="Форма")
    attribute_values_4: str = Field(description="Значения атрибутов 4")
    visibility_attribute_4: int = Field(description="Видимость атрибута 4", default=0)
    global_attribute_4: int = Field(description="Глобальный атрибут 4", default=1)


class FinalTableWithVariations(BaseModel):
    id: str = Field(description="ID")
    type: str | None = Field(description="Тип", default=None)
    article: int | None = Field(description="Артикул", default=None)
    name: str | None = Field(description="Имя", default=None)
    published: int | None = Field(description="Опубликован", default=None)
    recommended: int | None = Field(description="рекомендуемый?", default=None)
    visibility_in_the_catalog: str | None = Field(description="Видимость в каталоге", default=None)
    short_description: str | None = Field(description="Краткое описание", default=None)
    description: str | None = Field(description="Описание", default=None)
    discount_start_date: str | None = Field(description="Дата начала действия скидки", default=None)
    discount_expiration_date: str | None = Field(description="Дата окончания действия скидки", default=None)
    tax_status: str | None = Field(description="Статус налога", default=None)
    tax_class: str | None = Field(description="Налоговый класс", default=None)
    availability: int | None = Field(description="В наличии?", default=None)
    stocks: int | None = Field(description="Запасы", default=None)
    size_of_small_stocks: str | None = Field(description="Величина малых запасов", default=None)
    pre_order: int | None = Field(description="Возможен ли предзаказ?", default=None)
    sold_individually: int | None = Field(description="Продано индивидуально?", default=None)
    weight: str | None = Field(description="Вес (kg)", default=None)
    length: str | None = Field(description="Длина (cm)", default=None)
    width: str | None = Field(description="Ширина (cm)", default=None)
    height: str | None = Field(description="Высота (cm)", default=None)
    feedback: int | None = Field(description="Разрешить отзывы от клиентов?", default=None)
    purchase_note: str | None = Field(description="Примечание к покупке", default=None)
    promotional_price: str | None = Field(description="Акционная цена", default=None)
    base_price: int | None = Field(description="Базовая цена", default=None)
    category: str | None = Field(description="Категории", default=None)
    tags: str | None = Field(description="Метки", default=None)
    delivery_class: str | None = Field(description="Класс доставки", default=None)
    images: str | None = Field(description="Изображения", default=None)
    download_limit: str | None = Field(description="Лимит загрузок", default=None)
    days_upload_period: str | None = Field(description="Дней срока загрузки", default=None)
    parent: str | None = Field(description="Родительский", default=None)
    grouped_products: str | None = Field(description="Сгруппированные товары", default=None)
    upsale: str | None = Field(description="Апсейл", default=None)
    crossels: str | None = Field(description="Кросселы", default=None)
    external_url: str | None = Field(description="Внешний URL", default=None)
    button_text: str | None = Field(description="Текст кнопки", default=None)
    position: int | None = Field(description="Позиция", default=None)
    attribute_name_1: str | None = Field(description="Название атрибута 1", default=None)
    attribute_values_1: str | None = Field(description="Значения атрибутов 1", default=None)
    visibility_attribute_1: int | None = Field(description="Видимость атрибута 1", default=None)
    global_attribute_1: int | None = Field(description="Глобальный атрибут 1", default=None)
    default_attribute_1: str | None = Field(description="Атрибут 1 по умолчанию", default=None)
    attribute_name_2: str | None = Field(description="Название атрибута 2", default=None)
    attribute_values_2: str | None = Field(
        description="Значения атрибутов 2", default=None
    )
    visibility_attribute_2: int | None = Field(description="Видимость атрибута 2", default=None)
    global_attribute_2: int | None = Field(description="Глобальный атрибут 2", default=None)
    default_attribute_2: str | None = Field(description="Атрибут 2 по умолчанию", default=None)
    attribute_name_3: str | None = Field(description="Название атрибута 3", default=None)
    attribute_values_3: str | None = Field(description="Значения атрибутов 3", default=None)
    visibility_attribute_3: int | None = Field(description="Видимость атрибута 3", default=None)
    global_attribute_3: int | None = Field(description="Глобальный атрибут 3", default=None)
    default_attribute_3: str | None = Field(description="Атрибут 3 по умолчанию", default=None)
    attribute_name_4: str | None = Field(description="Название атрибута 4", default=None)
    attribute_values_4: str | None = Field(description="Значения атрибутов 4", default=None)
    visibility_attribute_4: int | None = Field(description="Видимость атрибута 4", default=None)
    global_attribute_4: int | None = Field(description="Глобальный атрибут 4", default=None)

class DistributedPictures(ImageParameters):
    new_path: str = Field(description="Полный путь распределения")

