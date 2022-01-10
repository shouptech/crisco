# Copyright (C) 2021 Mike Shoup
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os

import yaml
import aiofiles
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse


app = FastAPI()


async def load_config():
    path = os.getenv("CRISCO_CONFIG_PATH")

    async with aiofiles.open(path, "r") as file:
        data = await file.read()

    return yaml.safe_load(data)


@app.get("/{path}", response_class=RedirectResponse)
async def get_path(path):
    config = await load_config()
    if path not in config["urls"]:
        raise HTTPException(status_code=404, detail="Path not found")
    return config["urls"][path]


@app.get("/", response_class=RedirectResponse)
async def get_root():
    config = await load_config()
    return config["urls"]["root"]
