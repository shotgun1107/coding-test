import re
solution = lambda s : s if (s := (re.sub("[a-c]", " ", s).split())) else ["EMPTY"]