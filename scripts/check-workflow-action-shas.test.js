const fs = require('node:fs');
const test = require('node:test');
const assert = require('node:assert/strict');

const buildWorkflow = fs.readFileSync('.github/workflows/build.yml', 'utf8');
const upgradeWorkflow = fs.readFileSync('.github/workflows/upgrade.yml', 'utf8');
const shaRef = '[0-9a-f]{40}';

test('build workflow pins external actions to full commit SHAs', () => {
  assert.match(buildWorkflow, new RegExp(`uses: pnpm/action-setup@${shaRef}`));
  assert.match(buildWorkflow, new RegExp(`uses: peaceiris/actions-hugo@${shaRef}`));
});

test('upgrade workflow pins external actions to full commit SHAs', () => {
  assert.match(upgradeWorkflow, new RegExp(`uses: pnpm/action-setup@${shaRef}`));
  assert.match(upgradeWorkflow, new RegExp(`uses: actions/setup-go@${shaRef}`));
  assert.match(upgradeWorkflow, new RegExp(`uses: peaceiris/actions-hugo@${shaRef}`));
});
