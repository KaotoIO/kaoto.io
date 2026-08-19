const fs = require('node:fs');
const test = require('node:test');
const assert = require('node:assert/strict');

const workflow = fs.readFileSync('.github/workflows/build.yml', 'utf8');

test('build workflow disables lifecycle scripts during dependency installation', () => {
  assert.match(workflow, /pnpm install --ignore-scripts --no-frozen-lockfile/);
  assert.match(workflow, /npm install --ignore-scripts/);
});

test('build workflow does not use npx fallback for pagefind', () => {
  assert.doesNotMatch(workflow, /\bnpx\b[^\n]*\bpagefind\b/);
  assert.match(workflow, /pnpm exec pagefind --site "public"/);
});
