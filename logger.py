import pandas as pd
from datetime import datetime
import os

def log_interaction(prompt, response, model_name):

    log_data = {
        "timestamp": [datetime.now()],
        "model": [model_name],
        "prompt": [prompt],
        "response": [response]
    }

    df = pd.DataFrame(log_data)

    os.makedirs("results", exist_ok=True)

    file_exists = os.path.exists("results/logs.csv")

    df.to_csv(
        "results/logs.csv",
        mode="a",
        header=not file_exists,
        index=False
    )