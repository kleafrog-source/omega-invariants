import type { AnalyzeResponse, OperatorsResponse } from "./types";

const API_BASE_URL = "http://localhost:8011";

export async function fetchOperators(): Promise<OperatorsResponse> {
  const response = await fetch(`${API_BASE_URL}/operators`);
  if (!response.ok) {
    throw new Error(`Failed to load operators: ${response.status}`);
  }
  return response.json() as Promise<OperatorsResponse>;
}

export async function analyzeText(input: {
  text: string;
  domain: string;
}): Promise<AnalyzeResponse> {
  const response = await fetch(`${API_BASE_URL}/analyze`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(input)
  });

  if (!response.ok) {
    throw new Error(`Analyze request failed: ${response.status}`);
  }

  return response.json() as Promise<AnalyzeResponse>;
}

export async function exportResult(
  format: "json" | "html",
  input: { text: string; domain: string }
): Promise<Blob> {
  const response = await fetch(`${API_BASE_URL}/export/${format}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(input)
  });

  if (!response.ok) {
    throw new Error(`Export request failed: ${response.status}`);
  }

  return response.blob();
}
