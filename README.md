
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
<img width="608" alt="image" src="https://github.com/user-attachments/assets/ef421bd6-26b7-431e-9485-f4269a8b3abf" />

<img width="593" alt="image" src="https://github.com/user-attachments/assets/e7ec4a6a-045a-4341-9351-2250b8b50457" />



   - Configure scaling, environment variables, and networking as needed.
   - Deploy and verify the app is running (test with the public URL). Click on the URL to see your app. Use any on of the endpoints described in README_APP.md, e.g:
       ```bash
      https://pokemonapp.yourcontainer.azurecontainerapps.io/pokemon/pikachu
     ```
     <img width="1048" alt="image" src="https://github.com/user-attachments/assets/a8f44f44-9494-4d16-8186-a91be0891ff6" />
     <img width="602" alt="image" src="https://github.com/user-attachments/assets/a9b0b04f-3196-4c68-8236-83285cb63474" />



3. **Expose via Azure API Management (APIM)**
   - In Azure Portal, create or use an existing API Management instance. Must be at minimum a Basic v1 instance. See the documentation: https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server
     
     <img width="784" alt="image" src="https://github.com/user-attachments/assets/01509d5a-b197-4538-ad51-0d90c2e7e25c" />

   - Add a new API, using the Container App’s URL as the backend.
  
     <img width="1054" alt="image" src="https://github.com/user-attachments/assets/5a4b424c-2779-4c1d-8859-80b622b74b02" />
   - Browse your Container App, and select the pokemon one.

     <img width="668" alt="image" src="https://github.com/user-attachments/assets/355fcc43-313a-447d-96a6-a81fc574c2c5" />

     <img width="623" alt="image" src="https://github.com/user-attachments/assets/e44a38dc-1319-4a02-80fe-f1c8507750db" />
  
   - If everything goes OK, you will see all the operations of the API:
     
     <img width="1073" alt="image" src="https://github.com/user-attachments/assets/d1d81f2c-8b39-49e1-a275-851710fca025" />




   - Set up authentication, rate limiting, and policies as needed. Uncheck the subscription key if you are in a test environment. Check it if you want to add an extra header with a key.
   <img width="763" alt="image" src="https://github.com/user-attachments/assets/6f65a870-3e4c-41db-9d21-76e20b357f5a" />

   - If you want to test the API, select Test > Select an operation > Add the value of the parameters if needed > Press Send
     <img width="662" alt="image" src="https://github.com/user-attachments/assets/944fe7d0-f45e-4a4b-9dc5-8bbea66387a3" />

     <img width="514" alt="image" src="https://github.com/user-attachments/assets/c2ad1e8b-b359-4480-b908-1f7ad8de8553" />


3. **Enable MCP Server in APIM (Preview)**
   - In APIM, enable the AI Gateway Early Update (Basic v1 tier or higher).

      <img width="1053" alt="image" src="https://github.com/user-attachments/assets/85d185ea-d227-4dec-9333-47751cf9e016" />

   - Export your API as a Model Context Protocol (MCP) server—no code changes required. In the Azure Portal, access the MCP Server preview at the following URL:
     ```bash
      https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp
     ```
   - You will see now a new menu:
     
      <img width="170" alt="image" src="https://github.com/user-attachments/assets/2da555e7-4c95-4607-9c38-7722aebfdb9d" />

   - Create a new MCP Server > Select Pokemon API > Select all the operation you want to have in your MCP Server active:

      <img width="573" alt="image" src="https://github.com/user-attachments/assets/6b32548c-3154-45fc-8370-68ff48a2c818" />

   - Get the MCP endpoint for AI-powered integrations:
     
      <img width="524" alt="image" src="https://github.com/user-attachments/assets/4501af11-c5c3-4c57-b85d-ef3f2203a6ef" />


4. **Test with GitHub Copilot**
   - Add a MCP Server in Github Copilot. You can see already created in .vscode/mcp.json. Copy and paste your endpoint, should look like:
     ```bash
      https://YOUR_APIM.azure-api.net/pokeapi-mcp/mcp
     ```
   - Run the server. Check the number of tools. You can see the docs here https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/get-started?tabs=one-click%2Cazure-cli&pivots=mcp-github-copilot
   - Use Copilot Chat to prompt and test your API features.
    ```bash
      Give me the info about Pikachu
     ```

---

## Useful Links

- [Azure APIM MCP Server](https://lnkd.in/dAwrSj2b)
- [Azure Container Apps docs](https://lnkd.in/dwSpBkrj)
- [Azure API Management docs](https://lnkd.in/degiP6_g)
- [PokeAPI](https://pokeapi.co/)

