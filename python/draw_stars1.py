def draw_stars(arr):
	for x in arr:
		if x is int:
			print '*'* x
		elif x is str:
			length=len(x)
			alpha= x[0].lower
			print length*letter
x=[4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]			
draw_stars(x)		
