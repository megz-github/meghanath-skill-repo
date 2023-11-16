"""If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d

like to invite to dinner. Then use your list to print a message to each person, invitingthem to dinner."""

guests = ["Albert Einstein", "Freddie Mercury", "Leonardo da Vinci"]

for guest in guests:
    invitation = f"Dear {guest}, I would like to invite you to dinner. Please join us for a wonderful evening."
    print(invitation)
