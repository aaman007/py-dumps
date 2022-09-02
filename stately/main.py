from copy import deepcopy
from collections import defaultdict
from typing import Union, Callable


class StateMachine:
    def __init__(self, initial_state: str):
        self._state = initial_state
        self._transitions = defaultdict(dict)
        self._finalize = False
    
    def get_state(self) -> str:
        return self._state
    
    def finalize(self):
        self._finalize = True
    
    def add_transition(
        self,
        from_state: str,
        to_state: str,
        processor: Callable,
        pre_hook: Union[Callable, None] = None,
        post_hook: Union[Callable, None] = None,
    ):
        if self._finalize:
            raise Exception('Transitions cannot be added once finalized')

        self._transitions[from_state][to_state] = {
            'processor': processor,
            'pre_hook': pre_hook,
            'post_hook': post_hook,
        }
    
    def will(self, next_state: str) -> bool:
        return next_state in self._transitions[self._state]
    
    def process(self, next_state: str):
        if not self._finalize:
            raise Exception('Finalize the machine before processing state changes')
        if not self.will(next_state):
            raise Exception('Invalid state transition')
        
        transition = self._transitions[self._state][next_state]
        
        transition['pre_hook'] and transition['pre_hook']()
        transition['processor']()
        self._state = next_state
        transition['post_hook'] and transition['post_hook']()


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
    
    def __get_field_instance(self, field):
        self.__verify_field(field)
        return Database.__FIELD_TO_TYPE[field]
    
    def __get_field_instance_name(self, field):
        return self.__get_field_instance(field).__name__

    def __verify_field(self, field):
        if not hasattr(self, field):
            raise Exception(f'Unknown table {field}')
    
    def __verify_item_type(self, field, item):
        self.__verify_field(field)
        if not isinstance(item, self.__get_field_instance(field)):
            raise Exception(f'Unsupported item for table {field}')
    
    def __get_index(self, field, id):
        self.__verify_field(field)

        index = next((index for index, item in enumerate(getattr(self, field)) if item.id == id), None)
        if index is None:
            raise Exception(f'{self.__get_field_instance_name(field)} with id {id} not found!')
        
        return index
    
    def find(self, field, id):
        index = self.__get_index(field, id)
        return deepcopy(getattr(self, field)[index])
            
    def insert(self, field, item):
        self.__verify_item_type(field, item)
        items = getattr(self, field)
        items.append(deepcopy(item))
        return item
    
    def update(self, field, id, item):
        self.__verify_item_type(field, item)
        items = getattr(self, field)
        index = self.__get_index(field, id)
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
        def sanitize_payload(payload):
            payload.pop('id', None)
            return payload
    
        app = cls.get(id)
        payload = sanitize_payload(payload)

        for attribute, value in payload.items():
            if attribute == 'status':
                raise ValueError('status should be updated separately')
            hasattr(app, attribute) and setattr(app, attribute, value)

        return db.update('applications', id, app)
    
    @classmethod
    def change_status(cls, id, status):
        def accept_pre_hook():
            print('Application Accepted Pre-Hook...')
        
        def accept_post_hook():
            print('Application Accepted Post-Hook...')

        def accept():
            print('Application Accepted...')
        
        def un_accept():
            print('Application Un-Accepted...')
        
        def reject():
            print('Application Rejected...')

        def un_reject():
            print('Application Un-Rejected...')

        def complete():
            print('Application Completed...')

        def un_complete():
            print('Application Un-Completed...')
        
        
        app = cls.get(id)
        current_status = app.status

        machine = StateMachine(current_status)
        machine.add_transition(
            'Submitted',
            'Accepted',
            accept,
            accept_pre_hook,
            accept_post_hook
        )
        machine.add_transition('Accepted', 'Submitted', un_accept)
        machine.add_transition('Submitted', 'Rejected', reject)
        machine.add_transition('Rejected', 'Submitted', un_reject)
        machine.add_transition('Accepted', 'Completed', complete)
        machine.add_transition('Completed', 'Accepted', un_complete)
        machine.finalize()
        
        if machine.will(status):
            machine.process(status)
            app.status = status
            db.update('applications', id, app)
        else:
            raise Exception(f'Invalid status transition {current_status} -> {status}')
    
        return app
        

if __name__ == '__main__':
    app = ApplicationService.create(
        dict(
            title='My App',
            data={'meta': 'Some meta'},
        )
    )
    ApplicationService.create(
        dict(
            title='My App 2',
            data={'meta': 'Some meta'},
        )
    )
    print(app.__dict__)
    print(ApplicationService.update(2, {'title': 'Some new title'}).__dict__)

    print(ApplicationService.get(1).__dict__)
    print(ApplicationService.change_status(1, 'Accepted').__dict__)
    print(ApplicationService.change_status(1, 'Completed').__dict__)
    print(ApplicationService.change_status(1, 'Accepted').__dict__)
    print(ApplicationService.change_status(1, 'Submitted').__dict__)
    print(ApplicationService.change_status(1, 'Rejected').__dict__)
    print(ApplicationService.change_status(1, 'Submitted').__dict__)
    print(ApplicationService.change_status(1, 'Accepted').__dict__)
