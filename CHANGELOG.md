# Change Log

## [1.0.3] 2022-11-05
### Improvements

- For static, load builder from ENV
  - `RENDER_BUILDER`: defaults to NPM
- Rename entry point
  - `runner` -> `deployer`
- `Update DOCS` (README)  

## [1.0.2] 2022-11-03
### Improvements

- Code refactoring 
- Improved Logging

## [1.0.1] 2022-11-03
### Improvements

- Code refactoring 
- Added `deploy_static` handler
- Update helpers (minor)

## [1.0.0] 2022-11-01
### STABLE (MINIMAL) Version

- Improved error checking
- Flask Deployment 
  - `python.exe .\runner.py deploy_flask <REPO> <ENTRY_POINT>`

## [0.0.1] 2022-11-01
### Initial Release

- Code the basic structure
- Added CLI input parser 
- Added helpers: `check`, `owner`
