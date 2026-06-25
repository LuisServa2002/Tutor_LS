import asyncio
import json
import websockets

async def enviar_prueba():
    """Conecta al WebSocket del servidor, envía landmarks y recibe la predicción."""
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        landmarks = [0.5] * 63
        message = {"landmarks": landmarks}
        await websocket.send(json.dumps(message))
        response = await websocket.recv()
        print(f"Respuesta del servidor: {response}")

if __name__ == "__main__":
    asyncio.run(enviar_prueba())
