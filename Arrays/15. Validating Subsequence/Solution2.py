def isValidSubsequence(array, sequence):
    # Write your code here.
    seqIdx = 0
	for value in array:
		if seqIdx == len(sequence):
			break
		if sequence[seqIdx] == value:
			seqIdx += 1
	return seqIdx == len(sequence)
