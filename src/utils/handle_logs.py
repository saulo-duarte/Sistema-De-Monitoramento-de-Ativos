import logging

class ListHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.logs = []

    def emit(self, record):
        try:
            # Utiliza a formatação padrão para o tempo
            formatter = self.formatter  # Acessa o formatador configurado
            log_entry = {
                "timestamp": formatter.formatTime(record),  # Usa o formatador para o tempo
                "level": record.levelname,
                "message": record.getMessage()
            }
            self.logs.append(log_entry)
        except Exception as e:
            self.handleError(record)

    def get_logs(self):
        return self.logs