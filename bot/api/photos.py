from typing import Optional
from uuid import UUID

from bot.schemas.photo import VkPhoto
from bot.settings import settings
import aiohttp


async def get_random_photo(token: UUID, ignore_groups: bool = False) -> Optional[VkPhoto]:
    url = settings.api_url + f"/photo/random?token={token}&ignoreGroups={ignore_groups}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as resp:
            if resp.status == 200:
                data = await resp.json()
                return VkPhoto(**data)
            if resp.status in [403, 404, 405]:
                return await resp.json()
            raise Exception('/photo/random bad request')
