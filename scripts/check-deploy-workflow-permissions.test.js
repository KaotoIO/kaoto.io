const fs = require('node:fs');
const test = require('node:test');
const assert = require('node:assert/strict');

const workflow = fs.readFileSync('.github/workflows/deploy.yml', 'utf8');

test('deploy workflow keeps write permissions at the deploy job level only', () => {
  assert.doesNotMatch(workflow, /^permissions:\n(?:.*\n)*?  pages: write/m);
  assert.doesNotMatch(workflow, /^permissions:\n(?:.*\n)*?  id-token: write/m);
  assert.match(workflow, /deploy:\n(?:.*\n)*?    permissions:\n      pages: write(?: .*?)?\n      id-token: write(?: .*?)?/m);
});
