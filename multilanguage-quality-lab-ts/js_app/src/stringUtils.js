/**
 * Devuelve true si s es palíndromo (ignora espacios y mayúsculas/minúsculas).
 */
function isPalindrome(s) {
  const cleaned = s.toLowerCase().replace(/\s+/g, '');
  if (cleaned === cleaned.split('').reverse().join('')) {
    return true;
  } else {
    return false;
  }
}

module.exports = { isPalindrome };