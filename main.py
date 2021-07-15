#!/usr/bin/python3

import time
import pandas as pd

if __name__ == "__main__":
    f = "PtpBaseline.csv"
    measures = []
    start = time.time()
    while time.time() - start < 300:
        measures.append(1e6*time.time())
        time.sleep(1)
    df = pd.DataFrame(measures)
    df.to_csv(f, ',', index=False)
