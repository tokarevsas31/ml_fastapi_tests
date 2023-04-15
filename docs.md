# ML FastAPI Application Documentation

This is a machine learning FastAPI application for sentiment analysis using the Hugging Face library.

## API Endpoints

### `GET /`

#### Description

Returns a simple "Hello World" message.

#### Response

- `200 OK`: JSON object with a "message" field containing the "Hello World" text.

### `POST /predict/`

#### Description

Takes an input text and returns the sentiment analysis result.

#### Parameters

- `text` (string): The input text for sentiment analysis.

#### Response

- `200 OK`: JSON object with "label" and "score" fields representing the sentiment result.

### `POST /predict_multiple/`

#### Description

Takes a list of input texts and returns the sentiment analysis results for each text.

#### Parameters

- `texts` (list of strings): A list of input texts for sentiment analysis.

#### Response

- `200 OK`: A list of JSON objects, each with "label" and "score" fields representing the sentiment results for each input text.
