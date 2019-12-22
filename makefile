all: test

test:
	python3 -m doctest mvstd/mvstd.py

upload:
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

clean:
	rm -rf mvstd.egg-info
	rm -rf mvstd/__pycache__
	rm -rf dist
	rm -rf build
