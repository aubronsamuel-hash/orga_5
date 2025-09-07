Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

pushd backend
pip install -e .[dev]
pytest
popd

pushd frontend
npm install
npm run lint
npm test
npx playwright install --with-deps
npm run playwright:smoke
popd
