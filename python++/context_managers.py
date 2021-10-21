import sys
import traceback
from contextlib import contextmanager


class Logger:
    def __enter__(self):
        print("Logger.__enter__(): Logging started")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Logger.__exit__(): Block executed without any error")
        else:
            print(f"Logger.__exit__(): Block raised an error - "
                  f"type:{exc_type} : reason:{exc_val}: traceback: {traceback.format_tb(exc_tb)}")
        print("Logger.__exit__(): Logging ended")
        return True


class ErrorLogger:
    def __init__(self, block_identifier):
        self.block_identifier = block_identifier

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Return True: To stop propagation of error i,e re-raising
        Return False or None: To propagate/re-raise the exception
        """

        if exc_type is not None:
            print(f"{self.block_identifier} block raised an error - "
                  f"type:{exc_type} : reason:{exc_val}: traceback: {traceback.format_tb(exc_tb)}")
        return True


@contextmanager
def logger_context_manager():
    print("logger_context_manager(): entered")
    try:
        yield 'Return value of context manager'
        print("logger_context_manager(): normal exit")
    except Exception:
        # could be re-raised
        print("logger_context_manager(): exceptional exist", sys.exc_info())
