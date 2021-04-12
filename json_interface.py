import json
import numpy as np
import dataclasses

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if dataclasses.is_dataclass(obj):
            return dataclasses.asdict(obj)
        elif isinstance(obj, np.ndarray):
            return list(obj)
        else:
            return super().default(obj)

def to_json(data):
    return json.dumps(data, cls=Encoder, indent=4)

def from_json(cls):
    def _f(data):
        return cls(**json.loads(data))
    return _f

