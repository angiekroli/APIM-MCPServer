# APIM-MCPServer

A simple FastAPI proxy server exposing custom endpoints over the PokeAPI. It allows you to get Pokémon info, images, and select random Pokémon by type.

## Main Features

- **/pokemon/{identifier}**: Returns detailed info about a Pokémon (name, id, types, abilities, stats, sprite, description).
- **/pokemon-image/{name}**: Redirects to the official Pokémon image.
- **/random-pokemon/{type}**: Returns up to 10 random Pokémon of the specified type.

## Dependencies

- fastapi >= 0.95.0
- uvicorn[standard] >= 0.22.0
- httpx >= 0.24.0

All dependencies are listed in `container/requirements.txt`.

## Recommended Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
pip install -r container/requirements.txt
```

## Local Run

From the `container` folder:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```


## Docker Usage

You can use the public image directly from Docker Hub:

```bash
docker pull angiekroli/pokeapi-proxy:latest
docker run -p 8000:8000 angiekroli/pokeapi-proxy:latest
```

Or build and run the container locally:

```bash
docker build -t pokeapi-proxy ./container
docker run -p 8000:8000 pokeapi-proxy
```

## File Structure

- `container/app.py`: Creates the FastAPI app and includes endpoints.
- `container/routes.py`: Defines the API endpoints.
- `container/requirements.txt`: Python dependencies.
- `container/Dockerfile`: Production-ready Docker image.


## Example Endpoints

- `GET /pokemon/pikachu`
  - `http://localhost:8000/pokemon/pikachu`
- `GET /pokemon-image/pikachu`
  - `http://localhost:8000/pokemon-image/pikachu`
- `GET /random-pokemon/electric`
  - `http://localhost:8000/random-pokemon/electric`

## Notes

- The exposed port is 8000.
- The server is ready for Azure Container Apps.

---
Author: Angelika Krolikowska