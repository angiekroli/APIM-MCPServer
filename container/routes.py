# Endpoint para obtener un Pokémon aleatorio por tipo
import random
from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse
import httpx
from fastapi.responses import RedirectResponse

router = APIRouter()

BASE_URL = "https://pokeapi.co/api/v2"

@router.get("/pokemon/{identifier}", response_class=PlainTextResponse)
async def get_pokemon(identifier: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/pokemon/{identifier.lower()}")
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail="Pokémon not found")
        data = resp.json()
        result = {
            "name": data["name"],
            "id": data["id"],
            "types": [t["type"]["name"] for t in data["types"]],
            "abilities": [a["ability"]["name"] for a in data["abilities"]],
            "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]},
            "sprite": data["sprites"]["other"]["official-artwork"]["front_default"]
        }
        species_resp = await client.get(data["species"]["url"])
        if species_resp.status_code == 200:
            species = species_resp.json()
            flavor = next(
                (f["flavor_text"] for f in species["flavor_text_entries"]
                 if f["language"]["name"] == "en"),
                None
            )
            if flavor:
                result["description"] = flavor.replace("\n", " ").replace("\f", " ")
        lines = [
            f"Name: {result['name']}",
            f"ID: {result['id']}",
            f"Types: {', '.join(result['types'])}",
            f"Abilities: {', '.join(result['abilities'])}",
            "Stats:",
        ]
        for stat, value in result["stats"].items():
            lines.append(f"  {stat}: {value}")
        lines.append(f"Sprite: {result['sprite']}")
        if "description" in result:
            lines.append(f"Description: {result['description']}")
        return "\n".join(lines)

# Endpoint para obtener solo la imagen de un Pokémon por nombre


@router.get("/pokemon-image/{name}")
async def get_pokemon_image(name: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/pokemon/{name.lower()}")
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail="Pokémon not found")
        data = resp.json()
        sprite_url = data["sprites"]["other"]["official-artwork"]["front_default"]
        if not sprite_url:
            raise HTTPException(status_code=404, detail="Image not found")
        return RedirectResponse(sprite_url)
    
@router.get("/random-pokemon/{type}", response_class=PlainTextResponse)
async def get_random_pokemon_by_type(type: str):
    async with httpx.AsyncClient() as client:
        type_resp = await client.get(f"{BASE_URL}/type/{type.lower()}")
        if type_resp.status_code != 200:
            raise HTTPException(status_code=type_resp.status_code, detail="Type not found")
        type_data = type_resp.json()
        pokemon_list = type_data.get("pokemon", [])
        if not pokemon_list:
            raise HTTPException(status_code=404, detail="No Pokémon found for this type")
        # Selecciona hasta 10 Pokémon aleatorios únicos
        sample_size = min(10, len(pokemon_list))
        random_pokemons = random.sample(pokemon_list, sample_size)
        names = [p["pokemon"]["name"] for p in random_pokemons]
        return "\n".join(names)
