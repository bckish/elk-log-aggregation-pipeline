import json
import random
import time
from datetime import datetime, timezone

services = ["api", "worker", "checkout"]
levels = ["INFO", "INFO", "INFO", "WARN", "ERROR"]

with open("/var/log/portfolio/application.json", "a", buffering=1) as stream:
    while True:
        level = random.choice(levels)
        event = {
            "@timestamp": datetime.now(timezone.utc).isoformat(),
            "service": random.choice(services),
            "level": level,
            "message": "request completed" if level != "ERROR" else "upstream dependency timeout",
            "request_id": f"req-{random.randint(1000, 9999)}",
        }
        stream.write(json.dumps(event) + "\n")
        time.sleep(1)
