
from fetch import *
import base64
import os
modules={}
def importLib(lib):
  try:
    modules[lib] = __import__(lib)
  except:
    eval("os.system(\"pip install "+lib+"\")")
    modules[lib] = __import__(lib)
  return modules[lib]


atob = zfetch('https://raw.githubusercontent.com/MaxArt2501/base64-js/master/base64.js').zread().decode("utf-8")
sval = zfetch('https://unpkg.com/sval@0.5.2/dist/sval.min.js').zread().decode("utf-8")

js2py=importLib("js2py");
def runCode(jscode):
  jscode=base64.b64encode(jscode.encode("utf-8")).decode("utf-8")
  print(jscode)
  return js2py.eval_js("""
  """+atob+"""
(function(){
  console.log(btoa);
Array.prototype.find = Array.prototype.find || function(callback) {
  if (this === null) {
    throw new TypeError('Array.prototype.find called on null or undefined');
  } else if (typeof callback !== 'function') {
    throw new TypeError('callback must be a function');
  }
  var list = Object(this);
  var length = list.length >>> 0;
  var thisArg = arguments[1];
  for (var i = 0; i < length; i++) {
    var element = list[i];
    if ( callback.call(thisArg, element, i, list) ) {
      return element;
    }
  }
};
try{
  if(!globalThis){
    this.globalThis=this;
  }
}catch(e){
  this.globalThis=this;
}

try{
  if(!global){
    this.global=this;
  }
}catch(e){
  this.global=this;
}

buildSval();
globalThis.options = {
  ecmaVer: 2019,
  sandBox: false
}


globalThis.interpreter = new Sval(globalThis.options);
globalThis.parse = globalThis.interpreter.parse;

function buildSval(){
  this.scope={};
  globalThis.console=console;
""" + sval +"""

}

return globalThis.interpreter.run(atob('"""+jscode+"""'));

})();
""")



runCode("""
let a = 'poop';
console.log(a);
""")

