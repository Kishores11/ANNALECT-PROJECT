import json
from json import JSONEncoder
from datetime import datetime, date, timedelta

data = {
    'date': date.today(),
    'datetime': datetime.now(),
    'timedelta': timedelta(hours=1)
}

class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        from datetime import datetime, date, timedelta

        if isinstance(o, (date, datetime)):
            return o.isoformat()
        if isinstance(o, timedelta):
            return o.total_seconds()
        return super().default(o)

encoder = CustomJSONEncoder
json_data = json.dumps(data, cls=encoder)

print(json_data)