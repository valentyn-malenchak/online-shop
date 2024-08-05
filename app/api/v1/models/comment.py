"""Module that contains comment domain models."""

from datetime import datetime
from typing import Annotated

from pydantic import BaseModel

from app.api.v1.models import BSONObjectId, ObjectId
from app.utils.pydantic import ObjectIdAnnotation


class Comment(BSONObjectId):
    """Thread comment model."""

    body: str
    thread_id: Annotated[ObjectId, ObjectIdAnnotation]
    user_id: Annotated[ObjectId, ObjectIdAnnotation]
    parent_comment_id: Annotated[ObjectId, ObjectIdAnnotation] | None
    path: str
    upvotes: int
    downvotes: int
    created_at: datetime
    updated_at: datetime | None


class BaseCommentCreateData(BaseModel):
    """Base thread comment create data model."""

    body: str
    parent_comment_id: Annotated[ObjectId, ObjectIdAnnotation] | None


class CommentCreateData(BaseModel):
    """Thread comment create data model."""

    body: str
    user_id: Annotated[ObjectId, ObjectIdAnnotation]
    thread_id: Annotated[ObjectId, ObjectIdAnnotation]
    parent_comment: Comment | None


class CommentUpdateData(BaseModel):
    """Comment update data model."""

    body: str
