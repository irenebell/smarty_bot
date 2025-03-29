import json

import aiofiles

import config


async def load_message(name: str) -> str:
    path = config.PATH_TO_MESSAGES / f"{name}.txt"
    async with aiofiles.open(path, mode="r", encoding="utf-8") as file:
        return await file.read()


async def load_image(name: str) -> bytes:
    path = config.PATH_TO_IMAGES / f"{name}.jpg"
    async with aiofiles.open(path, mode="rb") as file:
        return await file.read()


async def load_menu(name: str) -> dict:
    path = config.PATH_TO_MENUS / f"{name}.json"
    async with aiofiles.open(path, encoding="utf-8") as file:
        content = await file.read()
        return json.loads(content)


async def load_prompt(name: str) -> str:
    path = config.PATH_TO_PROMPTS / f"{name}.txt"
    async with aiofiles.open(path, mode="r", encoding="utf-8") as file:
        return await file.read()