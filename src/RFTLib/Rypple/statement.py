import re

from RFTLib.Core.Structure import *



statementRegex = re.compile(r"^\s*(?P<command>[\w_]+[\w\d_]*)?\s*:\s*(?P<variable>[\w_]+[\w\d_]*)?\s*:\s*(?P<value>.+)?$")



with open("test.ryp", "r") as file:
	for line in file.readlines():
		l = line.strip()


		if (l):
			if (not l.startswith("#")):
				statement = RFT_Structure()

				m = statementRegex.match(l)
				if (m):
					statement += m.groupdict()

				print(statement.toDict())


				prevC = None

				for c in l:
					if (prevC == "\\"):
						...

					else:
						if (c == "\""):
							if (dq % 2 == 0):
								dq -= 1
								quotes.append(quote)

							else:
								dq += 1
								quote = ""


					if (c not in "\"\'"):
						if (dq % 2 == 0):
							quote += c

					prevC = c


		quote += "\n"



	print(quotes)

