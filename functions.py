FILEPATH = "logs.json"

def get_logs(filepath=FILEPATH):
    """Read a text file and return the list of
    task items"""
    with open(filepath, "r") as file:
        logs = file.readlines()
    return logs

def write_logs(logs_arg, filepath=FILEPATH):
    """Write the task items list in the text file"""
    with open(filepath, "w") as file:
        file.writelines(logs_arg)
