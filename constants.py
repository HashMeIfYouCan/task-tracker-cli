class Status:
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"

class Command:
    ADD = "add"
    LIST = "list"
    DELETE = "delete"
    UPDATE = "update"
    MARK = "mark"
    HELP = "--help"

class Task:
    ID = "id"
    DESCRIPTION = "description"
    STATUS = "status"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"
