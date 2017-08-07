import sys, os
if len(sys.argv) > 1: dir = sys.argv[1]
if len(sys.argv) > 2: search = sys.argv[2]
matches = []
i, y = 0, 0

print()
if 'dir' in locals() and 'search' in locals():
	for filename in os.listdir(dir):
		path = dir + '\\' + filename
		with open(path) as f: content = f.readlines()
		content = [x.strip() for x in content]
		while y < len(content):
			if content[y].find(search) != -1: matches.append(path)
			y += 1
		y = 0
			
	print('Results:')
	print('========')
	if not matches: print('No matches found.')
	else:
		while i < len(matches):
			print(matches[i])
			i += 1
else: print('You must enter both parameters.\nEx. python main.py C:\path\\to\directory "pattern match"')