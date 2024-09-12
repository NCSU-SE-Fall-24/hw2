alias activate_venv='source venv/bin/activate'
alias pylint_files='python -m pylint hw2_debugging.py rand.py tests/ --output-format=colorized 2>&1 | tee -a post_traces/pylint/$(date +"%Y%m%d_%H%M%S")_output.txt'
alias pyflakes_files='python -m pyflakes hw2_debugging.py rand.py 2>&1 | tee -a post_traces/pyflakes/$(date +"%Y%m%d_%H%M%S")_output.txt'
alias autopep8_files='python -m autopep8 --diff -r --aggressive --aggressive hw2_debugging.py rand.py tests'