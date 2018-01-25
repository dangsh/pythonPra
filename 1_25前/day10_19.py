import shelve

db = shelve.open("shujuku");
print(db);
print(len(db));