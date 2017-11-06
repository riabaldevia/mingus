from mingus.containers import Note

Note("C") #default C is the 4th octave
'C-4'

Note("C", 4)
'C-4'

Note("C", 5) #5 notes 5th octave
'C-5'

n = Note()
n.set_note("C", 5)
n
'C-5'

Note("C", 6) #6th

