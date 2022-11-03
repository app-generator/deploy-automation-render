# [Render API Wrapper](https://www.youtube.com/watch?v=RRbmOhTzkYo) - `Python`

Python wrapper for [Render](https://render.com/) Deployment API - actively supported by **[AppSeed](https://appseed.us/)**.

<br />

> `Roadmap` - see [VIDEO Presentation](https://www.youtube.com/watch?v=RRbmOhTzkYo)

| Item | Python | Info |
| --- | --- | --- |
| Deploy Static Site | ✅ | [docs](./docs/python/deploy-static.md) |
| Deploy Web Service `Flask` | ✅ | [docs](./docs/python/deploy-flask.md) |
| Deploy Web Service `Django` | ❌ | - |

<br />

## How to use it

> Install modules

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> Export Variables

```bash
$ # Unix / MacOs 
$ export RENDER_API_KEY=<RENDER_API_KEY>     # mandatory
$ export RENDER_OWNER_ID=<RENDER_OWNER_ID>   # optional
$ export DEBUG=1                             # enables verbose output
$
$ # Windows - CMD 
$ set RENDER_API_KEY=<RENDER_API_KEY>        # mandatory
$ set RENDER_OWNER_ID=<RENDER_OWNER_ID>      # optional
$ set DEBUG=1                                # enables verbose output
$
$ # Windows - Powershell
$ $env:RENDER_API_KEY = "<RENDER_API_KEY>"   # mandatory
$ $env:RENDER_OWNER_ID = "<RENDER_OWNER_ID>" # optional
$ $env:DEBUG = "1"                           # enables verbose output
```

<br />

> EXEC API

| Item | Info | Sample Output | HELP |
| --- | --- | --- | --- |
| `python .\runner.py` | CLI Help | `Usage: runner.py COMMAND ARGS` | - |
| `python .\runner.py check` | Print API_KEY | `rnd_TgNuy1N*****` | - |
| `python .\runner.py all_owners` | Print all owners | `['usr-ccteupaen****', 'tea-ccts5053t398****']` | - |
| `python .\runner.py owner` | Get First Owner | `rnd_TgNuy1N*****` | - |
| --- | --- | --- | --- |
| `python .\runner.py deploy_flask REPO_URL` | Deploy Flask APP | ` > Deploy ID [dep-cdgjfbien0hj5ea9cbm0]` | - |
| --- | --- | --- | --- |
| `python .\runner.py deploy_static REPO_URL` | Deploy React, Vue | ` > Deploy ID [dep-cdgjfbien0hj5ea9cbm0]` | - |

<br />

---
[Render API Wrapper](https://www.youtube.com/watch?v=RRbmOhTzkYo) - Free tool provided by [AppSeed](https://appseed.us/)
