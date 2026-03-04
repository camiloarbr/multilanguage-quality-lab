const { isPalindrome } = require('../src/stringUtils');

test('radar es palíndromo', () => {
  expect(isPalindrome('radar')).toBe(true);
});

test('Radar con mayúscula es palíndromo', () => {
  expect(isPalindrome('Radar')).toBe(true);
});

test('anita lava la tina es palíndromo', () => {
  expect(isPalindrome('anita lava la tina')).toBe(true);
});

test('python no es palíndromo', () => {
  expect(isPalindrome('python')).toBe(false);
});

test('cadena vacía es palíndromo', () => {
  expect(isPalindrome('')).toBe(true);
});