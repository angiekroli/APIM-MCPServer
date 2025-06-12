
# Level Up Your Pokémon App with Azure: Step-by-Step Guide

This guide shows how to modernize your FastAPI Pokémon app using Docker, Azure Container Apps, API Management (APIM), and the Model Context Protocol (MCP) Server.

## Steps to Deploy and Expose Your App

1. **Containerize the App**
   - Write a `Dockerfile` for your FastAPI app (see `container/Dockerfile`).
   - Build the image locally:
     ```bash
     docker build -t angiekroli/pokeapi-proxy:latest ./container
     ```
   - (Optional) Push to Docker Hub:
     ```bash
     docker push angiekroli/pokeapi-proxy:latest
     ```

2. **Deploy to Azure Container Apps**
   - Go to Azure Portal > Container Apps.
   - Create a new Container App and use the public image `angiekroli/pokeapi-proxy:latest`.
   - Configure scaling, environment variables, and networking as needed.
   - Deploy and verify the app is running (test with the public URL).

3. **Expose via Azure API Management (APIM)**
   - In Azure Portal, create or use an existing API Management instance.
   - Add a new API, using the Container App’s URL as the backend.
   - Set up authentication, rate limiting, and policies as needed.
   - Publish the API to get a single public endpoint for all your routes.

4. **Enable MCP Server in APIM (Preview)**
   - In APIM, enable the AI Gateway Early Update (Basic v1 tier or higher).
   - Export your API as a Model Context Protocol (MCP) server—no code changes required.
   - Get the MCP endpoint for AI-powered integrations.

5. **Test with GitHub Copilot**
   - Use Copilot Chat to prompt and test your API features.
   - Copilot can call the MCP server endpoint through APIM for quick, AI-driven testing.

---

## Useful Links

- [Azure APIM MCP Server](https://lnkd.in/dAwrSj2b)
- [Azure Container Apps docs](https://lnkd.in/dwSpBkrj)
- [Azure API Management docs](https://lnkd.in/degiP6_g)
- [PokeAPI](https://pokeapi.co/)

