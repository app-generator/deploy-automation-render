# [Render API Wrapper](https://www.youtube.com/watch?v=RRbmOhTzkYo) - `Python`

Python wrapper for [Render](https://render.com/) Deployment API - actively supported by **[AppSeed](https://appseed.us/)**.

<br />

> `Roadmap` - see [VIDEO Presentation](https://www.youtube.com/watch?v=RRbmOhTzkYo)

| Item | Python | Info |
| --- | --- | --- |
| Deploy Static Site          | ✅ | [docs](./docs/python/deploy-static.md) |
| Deploy Web Service `Flask`  | ✅ | [docs](./docs/python/deploy-flask.md)  |
| Deploy Web Service `Django` | ✅ | [docs](./docs/python/deploy-django.md) |
| Deploy Web Service `NodeJS` | ✅ | [docs](./docs/python/deploy-nodejs.md) |
| --- | --- | --- |
| `AppSeed Specific` | --- | --- |
| Deploy `Flask API` Service  | ✅ | [docs](./docs/python/deploy-flask-api.md)  |
| Deploy `Django API` Service | ✅ | [docs](./docs/python/deploy-django-api.md) |
| Deploy `NodeJS API` Service | ✅ | [docs](./docs/python/deploy-nodejs-api.md) |

<br />

## How to use it

> Install modules

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

### Export Variables

> Unix / MacOs `environment`

```bash
$ export RENDER_API_KEY=<RENDER_API_KEY>     # mandatory
$ export RENDER_OWNER_ID=<RENDER_OWNER_ID>   # optional
$ export RENDER_BUILDER='npm'                # optional, <NPM or YARN>, defaults to NPM
$ export DEBUG=1                             # enables verbose output
```

<br />

> Windows CMD `environment`

```bash
$ set RENDER_API_KEY=<RENDER_API_KEY>        # mandatory
$ set RENDER_OWNER_ID=<RENDER_OWNER_ID>      # optional
$ set RENDER_BUILDER='npm'                   # optional, <NPM or YARN>, defaults to NPM
$ set DEBUG=1                                # enables verbose output
```

<br />

> Windows Powershell `environment`

```bash
$ $env:RENDER_API_KEY = "<RENDER_API_KEY>"   # mandatory
$ $env:RENDER_OWNER_ID = "<RENDER_OWNER_ID>" # optional
$ $env:RENDER_BUILDER = "npm"                # optional, <NPM or YARN>, defaults to NPM
$ $env:DEBUG = "1"                           # enables verbose output
```

<br />

### EXEC API

| Item | Info | Sample Output | HELP |
| --- | --- | --- | --- |
| `python deployer.py` | CLI Help | `Usage: runner.py COMMAND ARGS` | - |
| `python deployer.py check` | Print API_KEY | `rnd_TgN***` | - |
| `python deployer.py all_owners` | Print all owners | `['usr-cct***', 'tea-cct***']` | - |
| `python deployer.py owner` | Get First Owner | `rnd_TgN***` | - |
| --- | --- | --- | --- |
| `python deployer.py nodejs REPO_URL` | Deploy NodeJS APP | ` > Deploy ID [dep-cdg***]` | - |
| --- | --- | --- | --- |
| `python deployer.py django REPO_URL` | Deploy Django APP | ` > Deploy ID [dep-cdg***]` | - |
| --- | --- | --- | --- |
| `python deployer.py flask REPO_URL` | Deploy Flask APP | ` > Deploy ID [dep-cdg***]` | - |
| --- | --- | --- | --- |
| `python deployer.py static REPO_URL` | Deploy React, Vue | ` > Deploy ID [dep-cdg***]` | - |
| --- | --- | --- | --- |
| `python deployer.py nodejs_api <REPO_URL>` | REPO: [NodeJS API](https://github.com/app-generator/api-server-nodejs) | ` > Deploy ID [dep-cdg***]` | [docs](./docs/python/deploy-nodejs-api.md) |
| `python deployer.py flask_api  <REPO_URL>` | REPO: [Flask API](https://github.com/app-generator/api-server-flask)   | ` > Deploy ID [dep-cdg***]` | [docs](./docs/python/deploy-flask-api.md)  |
| `python deployer.py django_api <REPO_URL>` | REPO: [Django API](https://github.com/app-generator/api-server-django) | ` > Deploy ID [dep-cdg***]` | [docs](./docs/python/deploy-django-api.md) |

<br />

---
[Render API Wrapper](https://www.youtube.com/watch?v=RRbmOhTzkYo) - Free Tool provided by [AppSeed](https://appseed.us/)
