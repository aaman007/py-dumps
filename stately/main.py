from copy import deepcopy


class Status:
    SUBMITTED = 'Submitted'
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'
    COMPLETED = 'Completed'


class Priority:
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class Application:
    current_id = 0

    def __init__(self, title, data = {}):
        Application.current_id += 1
        self.id = Application.current_id
        self.title = title
        self.status = Status.SUBMITTED
        self.priority = Priority.LOW
        self.data = data


class Database:
    __FIELD_TO_TYPE = {
        'applications': Application,
    }
    
    def __init__(self):
        self.applications = []
    
    def __verify_field(self, field):
        if not hasattr(self, field):
            raise Exception(f'Unknown table {field}')
    
    def __verify_item_type(self, field, item):
        self.__verify_field(field)

        if not isinstance(item, Database.__FIELD_TO_TYPE[field]):
            raise Exception(f'Unsupported item for field {field}')
    
    def find(self, field: str, id: int):
        self.__verify_field(field)
        
        for item in getattr(self, field):
            if item.id == id:
                return deepcopy(item)
        
        raise Exception(f'{Database.__FIELD_TO_TYPE[field].__name__} with id {id} not found!')
    
    def insert(self, field, item):
        self.__verify_item_type(field, item)
        items = getattr(self, field)
        items.append(deepcopy(item))
        return item
    
    def update(self, field, id, item):
        self.__verify_item_type(field, item)
        items = getattr(self, field)

        index = next((index for index, item in enumerate(items) if item.id == id), None)
        if index is None:
            raise Exception(f'{Database.__FIELD_TO_TYPE[field].__name__} with id {id} not found!')

        items[index] = deepcopy(item)
        return item



db = Database()


class ApplicationService:
    
    @staticmethod
    def get(id):
        return db.find('applications', id)

    @staticmethod
    def create(payload):
        app = Application(**payload)
        db.insert('applications', app)
        return app
    
    @classmethod
    def update(cls, id, payload):
        app = cls.get(id)

        for attribute, value in payload.items():
            if attribute == 'id':
                raise ValueError('id cannot be updated')
            hasattr(app, attribute) and setattr(app, attribute, value)

        return db.update('applications', id, app)
    

if __name__ == '__main__':
    app = ApplicationService.create(
        dict(
            title='My App',
            data={'meta': 'Some meta'},
        )
    )
    print(app.__dict__)
    print(ApplicationService.get(1).__dict__)
    print(ApplicationService.update(1, {'status': 'Accepted'}).__dict__)