# htpt

A minimal FastAPI service that always responds with **HTTP 418 I'm a Teapot**:

```json
{
  "error": "I'm a teapot",
  "status": 418,
  "message": "The server refuses to brew coffee because it is, permanently, a teapot."
}
```

## Run

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run fastapi dev
```

The app runs at <http://127.0.0.1:8000>. For production, use `uv run fastapi run`.

## Behavior

`GET /{path:path}` is a catch-all route: `/`, `/coffee`, and `/a/b` all return the same `418` response. The request path is not echoed. Other HTTP methods return `405`.

The built-in docs at `/docs`, `/redoc`, and `/openapi.json` return `200`.

## License

[MIT](LICENSE)
