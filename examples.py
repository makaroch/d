# Application может определить интерфейс. 
# Но ничего не знать о том, где физически хранятся данные.
class UserRepositoryContract:
    pass


class OrderRepositoryContract:
    pass


# Для бизнес-логики все эти варианты выглядят одинаково.
# Она просто вызывает:

order_repository.get(id=id, ...)
order_Repository.save(order=order, ...)


























from dataclasses import dataclass

@dataclass
class User:
    pass


class UserRepository:
    async def get_by_id(self, user_id: UUID) -> User: ...

    async def get_by_name(self, name: str) -> User: ...

    async def get_by_email(self, email: str) -> User: ...

    async def get_by_username(self, username: str) -> User: ...

    async def get_by_name_and_email(
        self,
        name: str,
        email: str,
    ) -> User: ...

    async def list_by_ids(
        self,
        ids: list[UUID],
    ) -> list[User]: ...

    async def list_by_names(
        self,
        names: list[str],
    ) -> list[User]: ...

    async def list_active(self) -> list[User]: ...

    async def list_active_by_role(
        self,
        role: Role,
    ) -> list[User]: ...

    async def list_created_after(
        self,
        dt: datetime,
    ) -> list[User]: ...

    async def list_created_between(
        self,
        start: datetime,
        end: datetime,
    ) -> list[User]: ...

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



        



# Вместо
class UserRepository:
    async def get_by_ids(): ...

    async def list_active_admins(): ...

    async def list_by_roles(): ...

    async def list_created_after(): ...

    async def list_by_department_and_role(): ...


class OrderRepositiry:
    async def get_by_ids(): ...

    async def list_created_after(): ...


user_repo.list_active_admins()
user_repo.list_by_roles()
user_repo.list_created_after()
user_repo.get_by_ids()

order_repo.get_by_ids()

# Получили
class BaseRepo():
    async def filter(**filters): ...


class UserRepository(BaseRepo):
    pass


class OrderRepository(BaseRepo):
    pass


user_repo.filter( role="admin", is_active=True, )

order_repo.filter( role__in=["admin", "manager"], )

user_repo.filter( created_at__gte=start, )

order_repo.filter( department="IT", role="developer", )


# types? 