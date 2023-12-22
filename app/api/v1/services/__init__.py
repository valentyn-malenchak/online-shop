"""Module that contains base service abstract class."""

import abc
from typing import Any, Dict, List

from bson import ObjectId


class BaseService(abc.ABC):
    """Base service for encapsulating business logic."""

    @abc.abstractmethod
    async def get_item_by_id(self, id_: ObjectId) -> Any:
        """Retrieves an item by its unique identifier.

        Args:
            id_ (ObjectId): The unique identifier of the item.

        Returns:
            Any: The retrieved item or None if not found.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.

        """
        raise NotImplementedError

    @abc.abstractmethod
    async def create_items(self, items: List[Dict[str, Any]]) -> List[ObjectId]:
        """Creates new items.

        Args:
            items (List[Dict[str, Any]]): The data for the new items.

        Returns:
            List[ObjectId]: The created items.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.

        """
        raise NotImplementedError

    @abc.abstractmethod
    async def delete_all_items(self) -> None:
        """Deletes all items.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.

        """
        raise NotImplementedError