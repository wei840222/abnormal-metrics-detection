# abnormal-metrics-detection
API for detecte abnormal metrics

## How to build?
```bash
pack build --builder=gcr.io/buildpacks/builder:v1 --publish wei840222/amd:1 --env GOOGLE_ENTRYPOINT="uvicorn main:app --host=0.0.0.0 --port=8080"
```

## How to deploy?
```bash
kn ksvc apply --image=wei840222/amd:1 amd
```
