# tsad
API for time series anomaly detection.

## How to install dependencies
```bash
pipenv install
```

## How to build?
```bash
pipenv requirements > requirements.txt
pack build --builder=gcr.io/buildpacks/builder:v1 --publish wei840222/abnormal-metrics-detection:1 --env GOOGLE_ENTRYPOINT="uvicorn main:app --host=0.0.0.0 --port=8080 --workers=4 --log-level=debug"
```

## How to deploy?
```bash
kn ksvc apply --image=wei840222/abnormal-metrics-detection:1 abnormal-metrics-detection
```

## How to deploy by tekton?
```bash
kubectl apply -k .tekton
```
