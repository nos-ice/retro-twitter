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
{
  "id": str,
  "content": str,
  "created_at": datetime,
}

Response (400 Bat request)
{
  state: str
}
