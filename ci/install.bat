py -3.7 -m venv venv
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
python -m pip install --upgrade .
python -m pip install --upgrade wheel
python -m pip install --upgrade twine
call deactivate
