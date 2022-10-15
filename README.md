# abnormal-metrics-detection
API for detecte abnormal metrics

## How to install dependencies
```bash
pipenv install
```

## How to build?
```bash
pipenv lock -r > requirements.txt
pack build --builder=gcr.io/buildpacks/builder:v1 --publish wei840222/amd:3 --env GOOGLE_ENTRYPOINT="uvicorn main:app --host=0.0.0.0 --port=8080 --workers=4 --log-level=debug"
```

## How to deploy?
```bash
kn ksvc apply --image=wei840222/amd:3 amd
```
