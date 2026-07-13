1. Напоминание про Clean Architecture (2–3 минуты)
Что такое Clean Architecture
Бизнес-логика — самая важная часть системы.
Она не должна зависеть от базы данных, фреймворка, очередей сообщений или UI.
Все зависимости направлены к центру системы (Dependency Rule).

Показать схему:

Interface
    └── Infrastructure
            └── Application
                    └── Domain

Кратко рассказать про каждый слой.

Domain

сущности;
бизнес-правила;
value objects;
доменные сервисы.

Отвечает на вопрос:

Как работает бизнес?

Application

Use Cases;
Commands;
Queries;
DTO;
интерфейсы репозиториев.

Отвечает на вопрос:

Что необходимо сделать?

Infrastructure

база данных;
очереди;
внешние API;
кэш;
логирование;
репозитории.

Interface

REST;
gRPC;
UI;
CLI.
2. Что такое Repository? (2 минуты)

Переход:

Мы уже несколько раз упоминали репозиторий, но пока не обсудили, что это такое.

Определение.

Репозиторий — это объект, который предоставляет доступ к сущностям предметной области, скрывая детали хранения данных.

Важно подчеркнуть:

Repository работает с сущностями, а не с SQL.

или

Repository представляет собой коллекцию доменных сущностей.

Application вообще не знает:

PostgreSQL;
MongoDB;
Redis;
SQLAlchemy;
ORM.

Он знает только

user = await user_repository.get(id=user_id)
3. Зачем нужен Repository? (1–2 минуты)

Без Repository

row = await session.execute(...)
user = User(...)

Application знает про SQL и ORM.

С Repository

user = await user_repository.get(id=user_id)

Application получает готовую сущность.

Можно закончить мыслью:

Application работает с бизнес-объектами, а не с механизмом хранения данных.

4. Проблема обычных Repository (2 минуты)

Практически во всех проектах появляется это.

class UserRepository:

    get_by_id()

    get_by_email()

    get_by_name()

    get_by_username()

    list_by_role()

    list_by_roles()

    list_by_department()

    list_by_department_and_role()

    list_by_department_and_role_and_status()

    list_active()

    list_created_after()

    list_created_between()

    ...

Комментарий:

Через некоторое время репозиторий содержит десятки, а иногда сотни методов.

Потому что каждый новый сценарий поиска становится новым методом.

5. Идея общего Repository (3 минуты)

Главная мысль.

Мы перестали описывать методы поиска и начали описывать условия поиска.

Вместо

list_active_admins()

list_by_roles()

list_created_after()

list_by_department_and_role()

получили

await repo.list(
    role="admin",
    is_active=True,
)

await repo.list(
    role__in=["admin", "manager"],
)

await repo.list(
    created_at__gte=start,
)

await repo.list(
    department="IT",
    role="developer",
)

Теперь интерфейс Repository практически не меняется.

6. Язык фильтрации (2 минуты)

Показать возможности.

await repo.list(
    id=user_id
)

await repo.list(
    username__in=[...]
)

await repo.list(
    age__gt=18
)

await repo.list(
    age__gte=18
)

await repo.list(
    age__lt=65
)

await repo.list(
    age__lte=65
)

await repo.list(
    deleted_at__is_null=True
)

await repo.list(
    email__ne="admin@mail.com"
)

await repo.list(
    username__ilike="alex%"
)

Можно показать таблицу.

Выражение	SQL
field=value	=
field__ne	!=
field__gt	>
field__gte	>=
field__lt	<
field__lte	<=
field__in	IN
field__not_in	NOT IN
field__is_null	IS NULL
field__like	LIKE
field__ilike	ILIKE
7. Generic Repository (2 минуты)

Показать базовый класс.

EntityT = TypeVar("EntityT")


class Repository(Generic[EntityT]):

    async def get(...) -> EntityT:
        ...

    async def list(...) -> list[EntityT]:
        ...

    async def create(...) -> EntityT:
        ...

    async def update(...) -> EntityT:
        ...

Потом

class UserRepository(Repository[User]):
    pass

class OrderRepository(Repository[Order]):
    pass

И показать результат.

user = await user_repo.get(id=id)
# User

users = await user_repo.list(...)
# list[User]

order = await order_repo.get(...)
# Order

Именно здесь стоит сделать акцент:

Несмотря на универсальную реализацию, разработчик не теряет типизацию. IDE подсказывает поля, а статический анализатор проверяет корректность возвращаемых типов.

8. Финальный вывод

Я бы завершил выступление тремя тезисами.

Clean Architecture

Repository изолирует бизнес-логику от способа хранения данных.

Общий Repository

Вместо десятков методов появился единый API.

Generic + язык фильтрации

Универсальная реализация не привела к потере типизации.

И закончить фразой, которая хорошо связывает все части доклада:

Мы не пытались сделать "умный" репозиторий. Мы сделали репозиторий, у которого стабильный интерфейс, декларативный язык фильтрации и строгая типизация. Благодаря этому бизнес-код работает с сущностями предметной области и не зависит ни от SQL, ни от ORM, ни от конкретной базы данных.

Такая структура хорошо выстраивает повествование: от общих архитектурных принципов к конкретной инженерной проблеме и затем к ее решению, при этом каждый следующий раздел логично вытекает из предыдущего.