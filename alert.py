"Send an alert using ntfy"

import sys
import json
import requests


def load_config(config):
    """Load config from a json file"""

    try:
        with open(config, "r", encoding="ascii") as f:
            hosts = json.load(f)
            return hosts

    except Exception as err:
        print(err)
        return []

    return []


def alarm(config, title, message):
    "Use public nfty server to send alert - urgent"

    nfty_details = load_config(config)

    if len(nfty_details) != 2:
        print("ERROR:Config file hasn't got two elements")
        sys.exit()

    server = nfty_details[0]
    topic = nfty_details[1]

    try:
        requests.post(
            server + topic,
            data=message,
            headers={"Title": title, "Priority": "urgent", "Tags": "warning,skull"},
            timeout=30,
        )
    except Exception as err:
        print(err)
        return False

    return True


def notify(config, title, message):
    "Use public nfty server to send non urgent notification"

    nfty_details = load_config(config)

    if len(nfty_details) != 2:
        print("ERROR:Config file hasn't got two elements")
        sys.exit()

    server = nfty_details[0]
    topic = nfty_details[1]

    try:
        requests.post(
            server + topic,
            data=message,
            headers={"Title": title, "Priority": "min", "Tags": "warning,skull"},
            timeout=30,
        )
    except Exception as err:
        print(err)
        return False

    return True


def main():
    "Extract data from command line and use it to send an alarm"
    sys.argv.pop(0)
    inputargs = sys.argv

    if len(inputargs) != 3:
        print(
            "Incorrect calling sequence , parameters should be config_file  title message"
        )
        sys.exit()

    config = inputargs[0]
    title = inputargs[1]
    message = inputargs[2]

    alarm(config, title, message)


if __name__ == "__main__":
    main()
