import os
from pathlib import Path
from domain import RepeatImages


def get_path(directory: Path, base_path_name: str) -> list[Path]:
    subdirectories = []

    parents = [directory]
    for name in directory.parents:
        parents.append(name)
    parents.append(directory)

    if directory.name == base_path_name:
        return [directory]

    for subdirectory in parents:
        subdirectories.append(subdirectory)
        if subdirectory.name == base_path_name:
            break

    return subdirectories[::-1]


def create_category(directory: Path, base_path_name: str) -> str:
    category = "Картины"

    for subdirectory in get_path(directory, base_path_name):
        category += f" > {subdirectory.name}"

    return category


def run_repeat_images(directory: Path, base_directory_name: str, images_parameters: dict[str, RepeatImages] = {}):
    sub_folders = []
    # Перебираем все папки в директории
    for file in directory.iterdir():
        category = create_category(directory, base_directory_name)

        if file.is_dir():
            sub_folders.append(file)

        if file.is_file():
            if file.name in images_parameters:
                repeat_image = images_parameters[file.name]
                repeat_image.category += f", {category}"
            else:
                repeat_image = RepeatImages(
                    name=str(file.name),
                    category=str(category),
                )
                images_parameters[file.name] = repeat_image

    for dir in list(sub_folders):
        sf, file = run_repeat_images(dir, base_directory_name)
        sub_folders.extend(sf)
        images_parameters.update(file)

    return sub_folders, images_parameters
