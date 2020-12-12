def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]

	for i in range(len(array)):
		runningProduct = 1
		for j in range(len(array)):
			if i != j:
				runningProduct *= array[j]
		products[i] = runningProduct
		
	return products