import { useEffect, useRef, useState, useCallback } from "react";

export function useWebSocket(url) {
  const wsRef = useRef(null);
  const [prediction, setPrediction] = useState(null);
  const [connected, setConnected] = useState(false);

  useEffect(() => {
    const ws = new WebSocket(url);
    wsRef.current = ws;

    ws.onopen = () => setConnected(true);
    ws.onclose = () => setConnected(false);
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.letra) setPrediction(data);
    };

    return () => ws.close();
  }, [url]);

  const sendLandmarks = useCallback((landmarks) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({ landmarks }));
    }
  }, []);

  return { prediction, connected, sendLandmarks };
}
