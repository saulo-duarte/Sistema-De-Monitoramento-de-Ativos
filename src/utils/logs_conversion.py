import re
import os
import json


def logs_to_json(logs):
    log_pattern = re.compile(r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - (?P<level>[A-Z]+) - (?P<message>.*)')
    json_logs = []
    
    for log in logs:
        match = log_pattern.match(log)
        if match:
            log_dict = {
                "timestamp": match.group("timestamp"),
                "level": match.group("level"),
                "message": match.group("message")
            }
            json_logs.append(log_dict)
    
    return json.dumps(json_logs, ensure_ascii=False, indent=4)

def convert_logs_to_json_file(logs_dir, output_file):
    logs = []
    for filename in os.listdir(logs_dir):
        if filename.endswith(".log"):
            with open(os.path.join(logs_dir, filename), 'r') as file:
                logs.extend(file.readlines())
    
    json_output = logs_to_json(logs)
    
    with open(output_file, 'w') as json_file:
        json_file.write(json_output)
    
    print(f"Logs converted to JSON and saved to {output_file}")


logs_directory = os.path.abspath('src/data_acquisition/logs')
output_json_file = 'src/data_acquisition/logs/logs.json'
convert_logs_to_json_file(logs_directory, output_json_file)