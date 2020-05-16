def minRewards(scores):
    # Write your code here.
 	rewards = [1 for _ in scores]
	for i in range(1, len(scores)):
		j = i - 1
		if scores[1] > scores[j]:
			rewards[i] = rewards[j] + 1
		else:
			while j >= 0 and scores[j] > scores[j + 1]:
				rewards[j] = max(rewards[j], rewards[j + 1] + 1)
				j -= 1
	return sum(rewards)
