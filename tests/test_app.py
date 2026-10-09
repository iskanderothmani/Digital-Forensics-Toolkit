import hashlib,tempfile,unittest
from pathlib import Path
from app import build_manifest
class ManifestTests(unittest.TestCase):
 def test_hash(self):
  with tempfile.TemporaryDirectory() as d:
   (Path(d)/"x.txt").write_text("hello")
   self.assertEqual(build_manifest(d)["files"][0]["sha256"],hashlib.sha256(b"hello").hexdigest())
 def test_empty(self):
  with tempfile.TemporaryDirectory() as d: self.assertEqual(build_manifest(d)["files"],[])
 def test_bad_path(self):
  with self.assertRaises(ValueError): build_manifest("does-not-exist-for-test")
if __name__=="__main__": unittest.main()
