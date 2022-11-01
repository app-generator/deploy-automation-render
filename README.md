# Render API Wrapper 

> Status: DEVELOPMENT

Python wrapper for Render Deployment API.

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
| `python .\runner.py` | CLI Help | `Usage: runner.py COMMAND Argument` | - |
| `python .\runner.py check` | Print API_KEY | `rnd_TgNuy1N*****` | - |
| `python .\runner.py all_owners` | Print all owners | `['usr-ccteupaen****', 'tea-ccts5053t398****']` | - |
| `python .\runner.py ****` | Get First Owner | `rnd_TgNuy1N*****` | - |
| --- | --- | --- | --- |
| `python .\runner.py deploy_flask REPO_URL` | Deploy Flask APP | ` > Deploy ID [dep-cdgjfbien0hj5ea9cbm0]` | - |

<br />

> Product Roadmap 

| Item | Python | Info |
| --- | --- | --- |
| Deploy Static Site (subdomain) | ❌ | - |
| Deploy Web Service `Flask` | ✅ | [docs](./docs/python/deploy-flask.md) |
| Deploy Web Service `Django` | ❌ | - |

<br />

---
Render API Wrapper  - Free tool provided by [AppSeed](https://appseed.us/)
