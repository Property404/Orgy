import operators

dictionary = {
	"objective": ["him", "her", "them", "it"],
	"reflexive": ["himself","herself", "themself", "itself"],
	"possessive": ["his", "her", "their", "its"],
	"possessive reflexive": ["his own", "her own", "their own", "its own"],
	"control flow": ["if", "while", "until", "end if", "more please", "declare safeword", "with safeword"],
	"context": ["have", "make", "times"],
}

# Add list of operators (primary and secondary names) to dictionary
dictionary.update({"operators": [a.name for a in operators.operators]+[a.alt for a in filter(
	lambda b: b is not None, operators.operators)]})

# Add list of comparison operator (primary and secondary names) to dictionary
dictionary.update({"comparison operators": [a.name for a in operators.comparison_operators]+[a.alt for a in filter(
	lambda b: b is not None, operators.comparison_operators)]})

# The list version of the dictionary: keywords
keywords = []
for a in [b for b in dictionary.values()]:
	for c in a:
		if c is not None:
			keywords.append(c)

# Every actual word that could be part of a meaning
base_words = (" ".join(keywords)).split()

# Just the pronouns, now
pronouns = dictionary["objective"] + dictionary["reflexive"] + dictionary ["possessive"] + dictionary["possessive reflexive"]
