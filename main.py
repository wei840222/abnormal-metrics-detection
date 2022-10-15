import logging
from fastapi import FastAPI, UploadFile, HTTPException
import pandas as pd
from adtk.data import validate_series
from adtk.detector import LevelShiftAD
from adtk.visualization import plot
from matplotlib import pyplot as plt
from io import BytesIO
from starlette.responses import StreamingResponse

logger = logging.getLogger("uvicorn.error")
app = FastAPI()

@app.get("/")
async def ping():
    return "pong"

@app.post("/adtk/level-shift-ad")
async def adtk_level_shift_ad(data: UploadFile):
    logger.debug(f"filename: {data.filename}, content_type: {data.content_type}")
    match data.content_type:
        case "text/csv":
            s_train = pd.read_csv(data.file, index_col="timestamp", parse_dates=True).squeeze()
        case _:
            raise HTTPException(status_code=400, detail="File type not supported")
    
    s_train = validate_series(s_train)
    logger.debug(f"request data\n{s_train}")

    level_shift_ad = LevelShiftAD(c=6.0, side='both', window=200)

    anomalies = level_shift_ad.fit_detect(s_train, return_list=True)
    logger.debug(f"anomalies: {anomalies}")

    fig, ax = plt.subplots(nrows=1, figsize=(16, 4 * 1), sharex=True)
    plot(s_train, anomaly=anomalies, ts_linewidth=1, ts_markersize=1, anomaly_color='red', axes=ax)

    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")