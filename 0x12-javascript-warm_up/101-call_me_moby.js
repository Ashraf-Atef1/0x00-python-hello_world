#!/usr/bin/node
function callMeMoby (x, theFunction) {
  while (0 < x--) {
    theFunction();
  }
}
module.exports = {
  callMeMoby
};
