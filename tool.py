"""Build stable SHA-256 request cache keys."""
from __future__ import annotations
import hashlib,json
def key(model:str,prompt:str,system:str='',options:dict|None=None)->str:
 payload={'model':model.strip(),'prompt':prompt.strip(),'system':system.strip(),'options':options or {}}
 encoded=json.dumps(payload,sort_keys=True,separators=(',',':'),ensure_ascii=True);return hashlib.sha256(encoded.encode()).hexdigest()
if __name__=='__main__':
 import json,sys;p=json.load(sys.stdin);print(key(p['model'],p['prompt'],p.get('system',''),p.get('options')))
