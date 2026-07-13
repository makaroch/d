from dataclasses import dataclass


@dataclass
class User:
    pass


class UserRepository:
    async def get_by_id(self, user_id: UUID) -> User:
        ...

    async def get_by_name(self, name: str) -> User:
        ...

    async def get_by_email(self, email: str) -> User:
        ...

    async def get_by_username(self, username: str) -> User:
        ...

    async def get_by_name_and_email(
        self,
        name: str,
        email: str,
    ) -> User:
        ...

    async def list_by_ids(
        self,
        ids: list[UUID],
    ) -> list[User]:
        ...

    async def list_by_names(
        self,
        names: list[str],
    ) -> list[User]:
        ...

    async def list_active(self) -> list[User]:
        ...

    async def list_active_by_role(
        self,
        role: Role,
    ) -> list[User]:
        ...

    async def list_created_after(
        self,
        dt: datetime,
    ) -> list[User]:
        ...

    async def list_created_between(
        self,
        start: datetime,
        end: datetime,
    ) -> list[User]:
        ...

    class UserRepository:
        # ...
        # спустя пару месяцев поддержкии добавяться еще....
        async def list_by_name_and_role(...)
        async def list_by_name_and_status(...)
        async def list_by_role_and_status(...)
        async def list_by_department(...)
        async def list_by_department_and_role(...)
        async def list_by_department_and_status(...)
        async def list_by_department_and_created_after(...)
        async def list_by_name_in(...)
        async def list_by_email_in(...)
        async def list_by_username_in(...)


