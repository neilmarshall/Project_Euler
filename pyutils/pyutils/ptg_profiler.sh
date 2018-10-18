#! /bin/bash
 
clear
python3 -c "import cProfile; \
            from pythagorean_triples import PythagoreanTripleGenerator; \
            cProfile.run('ptg = PythagoreanTripleGenerator()\nfor _ in range(10000): ptg.GetNextTriple()', sort='time')"
 
