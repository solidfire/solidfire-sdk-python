rm blackduck-python.zip
rm -r blackduck/

cd ../solidfire-api-descriptors
powershell ./GenerateDownstreamLocal.ps1 python
cd -

mkdir -p blackduck/srclib

cd blackduck/srclib

cp ../../__init__.py .
cp ../../setup.cfg .
cp ../../setup.py .
cp ../../README.md .

cp -r ../../solidfire .

cd ../../

zip -r blackduck-python.zip blackduck/	