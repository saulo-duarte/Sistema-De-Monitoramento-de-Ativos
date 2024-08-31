import logging

class ListHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.logs = []

    def emit(self, record):
        try:
            # Formatação do log
            log_entry = self.format(record)
            self.logs.append(log_entry)
        except Exception as e:
            self.handleError(record)

    def get_logs(self):
        return self.logs