def read_log():
    with open("logs.txt", "r") as file:
        logs = file.readlines()

    return logs

def write_logs(logs):
    with open("logs.txt", "w") as file:
        file.writelines(f"{logs}")

    return logs

def make_log(amount, type, description, time):
    log = {"Amount": amount, "Type": type, "Description": description, "Time": time}

    return log
