all: test

test:
	python3 -m doctest mvstd/mvstd.py
	rm -rf tmp
	mkdir -p tmp
	touch "tmp/the-MATRIX.mp4"
	touch "tmp/1977-10-23 00.11.22 orchid petals.jpg"
	python3 mvstd/mvstd.py --scene tmp/*
	test -f "tmp/The.Matrix.mp4"
	test -f "tmp/1977.10.23T001122.Orchid.Petals.jpg"
	touch "tmp/the-MATRIX.mp4"
	touch "tmp/1977-10-23 00.11.22 orchid petals.jpg"
	python3 mvstd/mvstd.py tmp/*
	test -f "tmp/the-matrix.mp4"
	test -f "tmp/1977-10-23T001122-orchid-petals.jpg"

upload:
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

clean:
	rm -rf tmp
	rm -rf mvstd.egg-info
	rm -rf mvstd/__pycache__
	rm -rf dist
	rm -rf build
