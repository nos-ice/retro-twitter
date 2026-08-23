GET /api/posts

用途
投稿一覧を時系列順で取得する

Request
{
    "id": str,
    "content": str,
    "created_at: datetime
}

Response (200 OK)

```json
{
  "messages": [
    {
      "id": "string",
      "content": "string",
      "created_at": "datetime"
    }
  ]
}

Response (400 Bat request)
{
  "state": str
}
