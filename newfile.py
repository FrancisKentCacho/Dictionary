import time
import sys

words = {
    "a": "the first letter of the alphabet",
    "about": "concerning or relating to",
    "above": "in a higher position than",
    "across": "from one side to the other",
    "after": "following in time or order",
    "again": "one more time",
    "against": "in opposition to",
    "all": "the whole quantity or number",
    "almost": "nearly but not quite",
    "also": "in addition",
    "always": "at all times",
    "and": "joining words or phrases",
    "another": "one more",
    "any": "one or some indiscriminately",
    "are": "the present tense of the verb 'to be'",
    "around": "in a circular direction",
    "as": "in the same way as",
    "at": "in or to a particular place or time",
    "be": "to exist",
    "because": "for the reason that",
    "been": "past participle of 'to be'",
    "before": "earlier in time or order",
    "being": "present participle of 'to be'",
    "below": "in a lower position than",
    "between": "in the space separating two things",
    "big": "of considerable size",
    "but": "indicating a contrast",
    "by": "through the agency of",
    "can": "to be able to",
    "come": "to move towards a particular place",
    "could": "past tense of 'can'",
    "day": "a period of 24 hours",
    "do": "to perform an action",
    "down": "in a lower position",
    "each": "every one of a number of people or things",
    "every": "all, without exception",
    "for": "with the purpose of",
    "from": "starting at a particular point",
    "get": "to obtain or receive",
    "go": "to move from one place to another",
    "good": "of high quality",
    "have": "to possess",
    "her": "belonging to or associated with a female person",
    "him": "belonging to or associated with a male person",
    "his": "belonging to or associated with a male person",
    "how": "in what way or manner",
    "if": "introducing a conditional clause",
    "in": "inside or within",
    "into": "to the inside of",
    "is": "the present tense of the verb 'to be'",
    "it": "referring to a thing previously mentioned or understood",
    "its": "belonging to or associated with something previously mentioned",
    "just": "only or simply",
    "know": "to be aware of something",
    "like": "to enjoy or find pleasure in",
    "look": "to direct one's eyes towards something",
    "make": "to create or produce",
    "many": "a large number",
    "me": "referring to the speaker",
    "more": "a greater quantity or number",
    "most": "the greatest quantity or number",
    "my": "belonging to or associated with me",
    "new": "recently made or created",
    "no": "not any",
    "not": "indicating negation",
    "now": "at this time",
    "of": "belonging to or associated with",
    "on": "in a position above and supported by something",
    "one": "the number 1",
    "only": "solely or exclusively",
    "or": "introducing an alternative",
    "other": "different from the one already mentioned",
    "our": "belonging to or associated with us",
    "out": "away from the inside of a place",
    "over": "above or across",
    "people": "human beings",
    "place": "a particular position or location",
    "put": "to move something to a particular position",
    "quite": "to a considerable degree",
    "really": "in fact or truth",
    "right": "correct or proper",
    "see": "to perceive with the eyes",
    "she": "referring to a female person",
    "so": "to such a degree",
    "some": "an unspecified number or quantity",
    "that": "referring to something previously mentioned",
    "the": "definite article",
    "their": "belonging to or associated with them",
    "them": "referring to people or things previously mentioned",
    "then": "at that time",
    "there": "in that place",
    "they": "referring to people or things previously mentioned",
    "this": "referring to something close at hand",
    "to": "indicating direction or purpose",
    "too": "to an excessive degree",
    "up": "in a higher position",
    "use": "to employ something for a particular purpose",
    "very": "to a great degree",
    "want": "to desire something",
    "was": "past tense of 'to be'",
    "we": "referring to the speaker and one or more other people",
    "were": "past tense of 'to be'",
    "what": "asking for information about something",
    "when": "at what time",
    "where": "in what place",
    "which": "asking for information about one or more of a number of things",
    "who": "asking for information about a person",
    "why": "asking for a reason",
    "will": "expressing future intention or certainty",
    "with": "in the company of",
    "would": "past tense of 'will'",
    "you": "referring to the person being addressed",
    "your": "belonging to or associated with you",
}


text = "English dictionary"

for a in text:
	sys.stdout.write(a)
	sys.stdout.flush()
	time.sleep(0.1)
	
print("\n")



b = input("Search: ").lower()


if b in words:
	print(b,"-", words[b])
	print("\n")
else:
	print("sorry the word", b, " is not found")
	print("\n")
	time.sleep(2)
		
print("\n")


while True:
	d = input("Anything else?: ").lower()
	if d in words:
		print(d, "-", words[d])
		print("\n")
	else:
			print("sorry the word", d, "is not found")
			print("\n")
			time.sleep(2)

	